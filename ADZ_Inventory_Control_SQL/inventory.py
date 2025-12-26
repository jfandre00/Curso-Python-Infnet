"""
Sistema simples de controle de inventário e custo de obra com sqlite3.
Comentários extensos explicam cada função. Sem dependências externas.
"""

import sqlite3
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import csv
import os

DB_FILE = "obra.db"

# --- Helpers de precisão monetária ---
def to_decimal(value):
    """Converte para Decimal com 2 casas (moeda)."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# --- Inicialização do banco ---
SCHEMA_SQL = open(os.path.join(os.path.dirname(__file__), "schema.sql")).read() if os.path.exists(os.path.join(os.path.dirname(__file__), "schema.sql")) else None

def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    # garante uso de strings para datas, etc.
    return conn

def init_db():
    """Cria as tabelas se não existirem. Se 'schema.sql' existir, use ele; caso contrário usa schema embutido."""
    schema = SCHEMA_SQL
    if schema is None:
        schema = """
        PRAGMA foreign_keys = ON;
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            name TEXT NOT NULL,
            unit TEXT NOT NULL,
            current_quantity REAL NOT NULL DEFAULT 0,
            unit_cost REAL NOT NULL DEFAULT 0,
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER NOT NULL REFERENCES materials(id) ON DELETE CASCADE,
            quantity REAL NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL,
            supplier TEXT,
            date TEXT DEFAULT (date('now')),
            note TEXT
        );
        CREATE TABLE IF NOT EXISTS usages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER NOT NULL REFERENCES materials(id) ON DELETE CASCADE,
            project_id INTEGER,
            task_id INTEGER,
            quantity REAL NOT NULL,
            unit_cost REAL NOT NULL,
            total_cost REAL NOT NULL,
            date TEXT DEFAULT (date('now')),
            note TEXT
        );
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            note TEXT
        );
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            name TEXT NOT NULL,
            note TEXT
        );
        CREATE TABLE IF NOT EXISTS stock_moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER NOT NULL REFERENCES materials(id) ON DELETE CASCADE,
            type TEXT NOT NULL,
            quantity REAL NOT NULL,
            reason TEXT,
            date TEXT DEFAULT (datetime('now'))
        );
        """
    conn = get_conn()
    with conn:
        conn.executescript(schema)
    conn.close()
    print("Banco inicializado em", DB_FILE)

# --- Operações em materiais ---
def add_material(code, name, unit, initial_qty=0, unit_cost=0):
    """Adiciona um novo material."""
    conn = get_conn()
    with conn:
        cur = conn.execute(
            "INSERT INTO materials (code, name, unit, current_quantity, unit_cost) VALUES (?, ?, ?, ?, ?)",
            (code, name, unit, float(initial_qty), float(unit_cost))
        )
        material_id = cur.lastrowid
    conn.close()
    return material_id

def get_material(material_id):
    conn = get_conn()
    cur = conn.execute("SELECT * FROM materials WHERE id = ?", (material_id,))
    row = cur.fetchone()
    conn.close()
    return row

def list_materials():
    conn = get_conn()
    cur = conn.execute("SELECT * FROM materials ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    return rows

# --- Compras (entrada de estoque) e média ponderada ---
def record_purchase(material_id, quantity, unit_price, supplier=None, date=None, note=None):
    """
    Registra uma compra (entrada) e atualiza estoque.
    Atualização de custo unitário usando média ponderada:
      novo_unit_cost = (estoque_antigo * custo_antigo + compra_qtd * unit_price) / (estoque_antigo + compra_qtd)
    """
    conn = get_conn()
    with conn:
        m = conn.execute("SELECT current_quantity, unit_cost FROM materials WHERE id = ?", (material_id,)).fetchone()
        if not m:
            raise ValueError("Material não encontrado")
        old_qty = Decimal(str(m["current_quantity"]))
        old_cost = Decimal(str(m["unit_cost"]))
        q = Decimal(str(quantity))
        up = to_decimal(unit_price)

        total_price = to_decimal(q * up)

        # calcula nova média ponderada
        if (old_qty + q) > 0:
            new_unit_cost = ((old_qty * old_cost) + (q * up)) / (old_qty + q)
            new_unit_cost = to_decimal(new_unit_cost)
        else:
            new_unit_cost = up

        # inserir purchase
        conn.execute(
            "INSERT INTO purchases (material_id, quantity, unit_price, total_price, supplier, date, note) VALUES (?,?,?,?,?,?,?)",
            (material_id, float(q), float(up), float(total_price), supplier, date or datetime.now().date().isoformat(), note)
        )

        # atualizar material: quantidade e unit_cost
        new_qty = float(old_qty + q)
        conn.execute(
            "UPDATE materials SET current_quantity = ?, unit_cost = ? WHERE id = ?",
            (new_qty, float(new_unit_cost), material_id)
        )

        # registrar movimento
        conn.execute(
            "INSERT INTO stock_moves (material_id, type, quantity, reason) VALUES (?,?,?,?)",
            (material_id, float(q), "in", f"Compra {supplier or ''}".strip())
        )
    conn.close()
    return True

# --- Uso / consumo de material ---
def record_usage(material_id, quantity, project_id=None, task_id=None, note=None, date=None):
    """
    Registra consumo do material, reduz estoque e grava custo baseado no unit_cost atual.
    """
    conn = get_conn()
    with conn:
        m = conn.execute("SELECT current_quantity, unit_cost FROM materials WHERE id = ?", (material_id,)).fetchone()
        if not m:
            raise ValueError("Material não encontrado")
        cur_qty = Decimal(str(m["current_quantity"]))
        if Decimal(str(quantity)) > cur_qty:
            # Você pode permitir estoque negativo, mas aqui nós bloqueamos
            raise ValueError(f"Estoque insuficiente. Em estoque: {cur_qty}")

        unit_cost = Decimal(str(m["unit_cost"]))
        q = Decimal(str(quantity))
        total_cost = to_decimal(unit_cost * q)

        # inserir usage
        conn.execute(
            "INSERT INTO usages (material_id, project_id, task_id, quantity, unit_cost, total_cost, date, note) VALUES (?,?,?,?,?,?,?,?)",
            (material_id, project_id, task_id, float(q), float(unit_cost), float(total_cost), date or datetime.now().date().isoformat(), note)
        )

        # atualizar estoque
        new_qty = float(cur_qty - q)
        conn.execute(
            "UPDATE materials SET current_quantity = ? WHERE id = ?",
            (new_qty, material_id)
        )

        # registrar movimento
        conn.execute(
            "INSERT INTO stock_moves (material_id, type, quantity, reason) VALUES (?,?,?,?)",
            (material_id, float(q), "out", f"Uso em projeto {project_id or ''} tarefa {task_id or ''}".strip())
        )
    conn.close()
    return True

# --- Projetos e tarefas ---
def create_project(name, start_date=None, end_date=None, note=None):
    conn = get_conn()
    with conn:
        cur = conn.execute(
            "INSERT INTO projects (name, start_date, end_date, note) VALUES (?,?,?,?)",
            (name, start_date, end_date, note)
        )
        pid = cur.lastrowid
    conn.close()
    return pid

def create_task(project_id, name, note=None):
    conn = get_conn()
    with conn:
        cur = conn.execute(
            "INSERT INTO tasks (project_id, name, note) VALUES (?,?,?)",
            (project_id, name, note)
        )
        tid = cur.lastrowid
    conn.close()
    return tid

# --- Relatórios básicos ---
def report_inventory():
    """Retorna lista de materiais com qty e valor total por item."""
    conn = get_conn()
    cur = conn.execute("SELECT id, code, name, unit, current_quantity, unit_cost, (current_quantity * unit_cost) as total_value FROM materials ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    return rows

def report_project_cost(project_id):
    """Soma total de custos (usages) por tarefa e total do projeto."""
    conn = get_conn()
    cur = conn.execute("""
        SELECT t.id as task_id, t.name as task_name,
               SUM(u.total_cost) as cost
        FROM tasks t
        LEFT JOIN usages u ON u.task_id = t.id
        WHERE t.project_id = ?
        GROUP BY t.id, t.name
        """, (project_id,))
    task_rows = cur.fetchall()
    total = sum([r["cost"] or 0 for r in task_rows])
    conn.close()
    return task_rows, total

# --- Export para CSV (por exemplo para abrir no Excel) ---
def export_inventory_csv(path="inventory_export.csv"):
    rows = report_inventory()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id","code","name","unit","current_quantity","unit_cost","total_value"])
        for r in rows:
            writer.writerow([r["id"], r["code"], r["name"], r["unit"], r["current_quantity"], r["unit_cost"], r["total_value"]])
    return path

# --- Funções utilitárias / exemplo de menu simples ---
def sample_data():
    """Insere alguns materiais e compra para testar."""
    m1 = add_material("CEM001", "Cimento CP-II", "saco", 0, 0)
    m2 = add_material("ARE001", "Areia média", "m3", 0, 0)
    record_purchase(m1, 50, 25.50, supplier="Fornecedor A")
    record_purchase(m2, 2.5, 120.0, supplier="Fornecedor B")
    print("Dados de exemplo inseridos.")

def simple_cli():
    init_db()
    while True:
        print("\n--- Menu ---")
        print("1 - Listar materiais")
        print("2 - Adicionar material")
        print("3 - Registrar compra")
        print("4 - Registrar uso")
        print("5 - Relatório inventário (tela + csv)")
        print("6 - Criar projeto + tarefa")
        print("7 - Relatório custo por projeto")
        print("0 - Sair")
        choice = input("Escolha: ").strip()
        if choice == "1":
            rows = list_materials()
            for r in rows:
                print(f"{r['id']}: {r['code']} - {r['name']} - {r['current_quantity']} {r['unit']} - R${r['unit_cost']}")
        elif choice == "2":
            code = input("Código: ")
            name = input("Nome: ")
            unit = input("Unidade (ex: un, m, m3): ")
            qty = float(input("Quantidade inicial: ") or 0)
            cost = float(input("Custo unitário inicial: ") or 0)
            add_material(code, name, unit, qty, cost)
            print("Material adicionado.")
        elif choice == "3":
            mid = int(input("ID do material: "))
            qty = float(input("Quantidade comprada: "))
            up = float(input("Preço unitário: "))
            supplier = input("Fornecedor (opcional): ")
            record_purchase(mid, qty, up, supplier=supplier)
            print("Compra registrada.")
        elif choice == "4":
            mid = int(input("ID do material: "))
            qty = float(input("Quantidade usada: "))
            pid = input("Projeto ID (opcional): ")
            tid = input("Tarefa ID (opcional): ")
            try:
                record_usage(mid, qty, int(pid) if pid else None, int(tid) if tid else None)
                print("Uso registrado.")
            except Exception as e:
                print("Erro:", e)
        elif choice == "5":
            path = export_inventory_csv()
            print("Exportado para", path)
            rows = report_inventory()
            for r in rows:
                print(f"{r['id']}: {r['name']} - {r['current_quantity']} {r['unit']} - Unit R${r['unit_cost']} - Total R${r['total_value']}")
        elif choice == "6":
            name = input("Nome do projeto: ")
            pid = create_project(name)
            print("Projeto criado com id", pid)
            tname = input("Nome da tarefa a criar (ou enter pular): ")
            if tname:
                tid = create_task(pid, tname)
                print("Tarefa criada com id", tid)
        elif choice == "7":
            pid = int(input("ID do projeto: "))
            tasks, total = report_project_cost(pid)
            for t in tasks:
                print(f"Tarefa {t['task_id']} - {t['task_name']} - Custo R${t['cost'] or 0}")
            print("TOTAL PROJETO: R$", total)
        elif choice == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    # se quiser executar o CLI simples
    simple_cli()
