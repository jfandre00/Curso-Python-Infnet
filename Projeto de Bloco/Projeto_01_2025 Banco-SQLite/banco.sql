.mode table

DROP TABLE IF EXISTS contas;

CREATE TABLE contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome CHAR(50),
    saldo REAL NOT NULL
);

INSERT INTO contas (nome, saldo) VALUES ('André', 100.00);
INSERT INTO contas (nome, saldo) VALUES ('Luise', 200.00);
INSERT INTO contas (nome, saldo) VALUES ('Murilo', 300.00);
INSERT INTO contas (nome, saldo) VALUES ('Gabriela', 400.00);

SELECT * FROM contas;
SELECT * FROM contas WHERE nome = 'André';