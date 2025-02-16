PRAGMA foreign_keys = ON;

--Modelo lógico das tabelas para SQLite

-- Tabela Contato
CREATE TABLE Contato (
    ID_Contato INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Data_Nascimento DATE NOT NULL
);

-- Tabela Endereco
CREATE TABLE Endereco (
    ID_Endereco INTEGER PRIMARY KEY,
    Rua TEXT NOT NULL,
    Numero INTEGER NOT NULL,
    Complemento TEXT,
    Bairro TEXT,
    Municipio TEXT NOT NULL,
    Estado TEXT NOT NULL,
    CEP TEXT NOT NULL,
    ID_Contato INTEGER NOT NULL,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Tabela Telefone
CREATE TABLE Telefone (
    ID_Telefone INTEGER PRIMARY KEY,
    Numero_Telefone TEXT NOT NULL UNIQUE,
    ID_Contato INTEGER NOT NULL,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Tabela Email
CREATE TABLE Email (
    ID_Email INTEGER PRIMARY KEY,
    Endereco_Email TEXT NOT NULL UNIQUE,
    ID_Contato INTEGER NOT NULL,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Adicionando 10 pessoas aleatórias na tabela Contato
INSERT INTO Contato (ID_Contato, Nome, Data_Nascimento) VALUES
(1, 'Maria Silva', '1985-05-15'),
(2, 'João Oliveira', '1990-02-20'),
(3, 'Ana Souza', '1978-07-10'),
(4, 'Carlos Pereira', '1982-03-25'),
(5, 'Mariana Lima', '1995-11-05'),
(6, 'Pedro Santos', '1988-09-15'),
(7, 'Fernanda Costa', '1992-01-30'),
(8, 'Lucas Rocha', '1980-04-12'),
(9, 'Julia Mendes', '1985-12-20'),
(10, 'Ricardo Souza', '1993-06-18')


-- Inserindo endereços aleatórios na tabela Endereco
INSERT INTO Endereco (ID_Endereco, Rua, Numero, Complemento, Bairro, Municipio, Estado, CEP, ID_Contato) VALUES
(1, 'Rua das Flores', 123, 'Apto 101', 'Jardim', 'São Paulo', 'SP', '01010-000', 1),
(2, 'Avenida Brasil', 456, '', 'Centro', 'Rio de Janeiro', 'RJ', '20020-000', 2),
(3, 'Rua do Sol', 789, 'Casa 3', 'Bela Vista', 'Belo Horizonte', 'MG', '30030-000', 3),
(4, 'Praça da Paz', 12, 'Bloco B', 'Copacabana', 'Rio de Janeiro', 'RJ', '22020-000', 4),
(5, 'Avenida Paulista', 234, '', 'Consolação', 'São Paulo', 'SP', '01310-000', 5),
(6, 'Rua das Laranjeiras', 567, 'Sala 201', 'Centro', 'Curitiba', 'PR', '80040-000', 6),
(7, 'Avenida dos Estados', 890, '', 'Centro', 'Porto Alegre', 'RS', '90010-000', 7),
(8, 'Rua dos Lírios', 345, 'Casa', 'Vila Nova', 'Fortaleza', 'CE', '60060-000', 8),
(9, 'Rua das Margaridas', 678, 'Apto 102', 'Jardim América', 'São Paulo', 'SP', '01410-000', 9),
(10, 'Avenida Independência', 910, '', 'Centro', 'Recife', 'PE', '50020-000', 10)

-- Inserindo telefones aleatórios na tabela Telefone
INSERT INTO Telefone (ID_Telefone, Numero_Telefone, ID_Contato) VALUES
(1, '(11) 99999-1111', 1),
(2, '(11) 99999-2222', 1), -- Contato com 2 telefones
(3, '(21) 88888-2222', 2),
(4, '(21) 88888-3333', 2), -- Contato com 3 telefones
(5, '(21) 88888-4444', 2),
(6, '(31) 77777-3333', 3),
(7, '(21) 66666-4444', 4),
(8, '(11) 55555-5555', 5),
(9, '(41) 44444-6666', 6),
(10, '(51) 33333-7777', 7),
(11, '(85) 22222-8888', 8),
(12, '(11) 11111-9999', 9),
(13, '(81) 00000-0000', 10), -- Contato com 2 telefones
(14, '(81) 00000-0001', 10); 


-- Inserindo emails aleatórios na tabela Email
INSERT INTO Email (ID_Email, Endereco_Email, ID_Contato) VALUES
(1, 'maria.silva@example.com', 1),
(2, 'maria.silva2@example.com', 1), -- Contato com 2 emails
(3, 'joao.oliveira@example.com', 2),
(4, 'ana.souza@example.com', 3),
(5, 'carlos.pereira@example.com', 4),
(6, 'mariana.lima@example.com', 5),
(7, 'pedro.santos@example.com', 6),
(8, 'pedro.santos2@examples.com', 6), -- Contato com 2 emails
(9, 'fernanda.costa@example.com', 7),
(10, 'lucas.rocha@example.com', 8),
(11, 'julia.mendes@example.com', 9),
(12, 'ricardo.araujo@example.com', 10)


-- Verificando os dados inseridos

SELECT * FROM Contato;
SELECT * FROM Endereco;
SELECT * FROM Telefone;
SELECT * FROM Email;

-- Consultar emails de um contato

SELECT c.Nome, e.Endereco_Email
FROM Contato c
JOIN Email e ON c.ID_Contato = e.ID_Contato
WHERE c.Nome = 'Maria Silva';

-- Consultar telefones de um contato

SELECT c.Nome, t.Numero_Telefone
FROM Contato c
JOIN Telefone t ON c.ID_Contato = t.ID_Contato
WHERE c.Nome = 'João Oliveira';

-- Consultar todos os dados de um contato

SELECT c.Nome, c.Data_Nascimento, e.Rua, e.Numero, e.Complemento, e.Bairro, e.Municipio, e.Estado, e.CEP, t.Numero_Telefone, em.Endereco_Email
FROM Contato c
JOIN Endereco e ON c.ID_Contato = e.ID_Contato
JOIN Telefone t ON c.ID_Contato = t.ID_Contato
JOIN Email em ON c.ID_Contato = em.ID_Contato
WHERE c.Nome = 'Ana Souza';

