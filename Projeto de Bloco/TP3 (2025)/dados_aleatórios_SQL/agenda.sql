-- Tabela Contato
CREATE TABLE Contato (
    ID_Contato INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Data_Nascimento DATE
);

-- Tabela Endereco
CREATE TABLE Endereco (
    ID_Endereco INTEGER PRIMARY KEY,
    Rua TEXT NOT NULL,
    Numero INTEGER,
    Complemento TEXT,
    Bairro TEXT,
    Municipio TEXT,
    Estado TEXT,
    CEP TEXT,
    ID_Contato INTEGER,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Tabela Telefone
CREATE TABLE Telefone (
    ID_Telefone INTEGER PRIMARY KEY,
    Numero_Telefone TEXT NOT NULL,
    ID_Contato INTEGER,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Tabela Email
CREATE TABLE Email (
    ID_Email INTEGER PRIMARY KEY,
    Endereco_Email TEXT NOT NULL,
    ID_Contato INTEGER,
    FOREIGN KEY (ID_Contato) REFERENCES Contato (ID_Contato)
);

-- Adicionando 20 pessoas aleatórias na tabela Contato
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
(10, 'Ricardo Araujo', '1993-06-18'),
(11, 'Paula Cardoso', '1987-08-24'),
(12, 'Bruno Almeida', '1983-10-07'),
(13, 'Camila Martins', '1991-05-28'),
(14, 'Gustavo Ferreira', '1975-12-01'),
(15, 'Larissa Ribeiro', '1989-03-14'),
(16, 'Renato Barbosa', '1994-07-22'),
(17, 'Patricia Moreira', '1986-11-30'),
(18, 'Roberto Teixeira', '1979-09-08'),
(19, 'Tatiane Gomes', '1992-02-18'),
(20, 'Fabio Correia', '1990-10-04');

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
(10, 'Avenida Independência', 910, '', 'Centro', 'Recife', 'PE', '50020-000', 10),
(11, 'Rua das Palmeiras', 123, 'Casa 4', 'Vila Mariana', 'São Paulo', 'SP', '04010-000', 11),
(12, 'Rua dos Girassóis', 456, '', 'Centro', 'Brasília', 'DF', '70040-000', 12),
(13, 'Avenida das Nações', 789, 'Bloco C', 'Asa Sul', 'Brasília', 'DF', '70200-000', 13),
(14, 'Rua do Comércio', 12, '', 'Centro', 'Salvador', 'BA', '40010-000', 14),
(15, 'Rua das Pedras', 234, 'Casa 2', 'Lagoa', 'Rio de Janeiro', 'RJ', '22430-000', 15),
(16, 'Avenida Central', 567, '', 'Centro', 'Florianópolis', 'SC', '88010-000', 16),
(17, 'Rua das Azaleias', 890, 'Apto 202', 'Vila Isabel', 'Rio de Janeiro', 'RJ', '20550-000', 17),
(18, 'Rua das Palmeiras', 345, 'Bloco A', 'Botafogo', 'Rio de Janeiro', 'RJ', '22220-000', 18),
(19, 'Avenida dos Andradas', 678, '', 'Savassi', 'Belo Horizonte', 'MG', '30120-000', 19),
(20, 'Rua dos Bambus', 910, 'Sala 301', 'Centro', 'Curitiba', 'PR', '80030-000', 20);

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
(13, '(81) 00000-0000', 10),
(14, '(81) 00000-1111', 10), -- Contato com 2 telefones
(15, '(11) 12345-6789', 11),
(16, '(61) 98765-4321', 12),
(17, '(61) 11223-4455', 13),
(18, '(71) 99887-6655', 14),
(19, '(21) 33445-6677', 15),
(20, '(48) 55667-7788', 16),
(21, '(21) 99888-7766', 17),
(22, '(21) 99888-7767', 17), -- Contato com 2 telefones
(23, '(21) 66554-4433', 18),
(24, '(31) 99876-5544', 19),
(25, '(41) 44332-2211', 20);

-- Inserindo emails aleatórios na tabela Email
INSERT INTO Email (ID_Email, Endereco_Email, ID_Contato) VALUES
(1, 'maria.silva@example.com', 1),
(2, 'maria.silva2@example.com', 1), -- Contato com 2 emails
(3, 'joao.oliveira@example.com', 2),
(4, 'ana.souza@example.com', 3),
(5, 'carlos.pereira@example.com', 4),
(6, 'mariana.lima@example.com', 5),
(7, 'pedro.santos@example.com', 6),
(8, 'fernanda.costa@example.com', 7),
(9, 'lucas.rocha@example.com', 8),
(10, 'julia.mendes@example.com', 9),
(11, 'ricardo.araujo@example.com', 10),
(12, 'paula.cardoso@example.com', 11),
(13, 'bruno.almeida@example.com', 12),
(14, 'camila.martins@example.com', 13),
(15, 'gustavo.ferreira@example.com', 14),
(16, 'larissa.ribeiro@example.com', 15),
(17, 'renato.barbosa@example.com', 16),
(18, 'patricia.moreira@example.com', 17),
(19, 'patricia.moreira2@example.com', 17), -- Contato com 2 emails
(20, 'roberto.teixeira@example.com', 18),
(21, 'tatiane.gomes@example.com', 19),
(22, 'tatiane.gomes2@example.com', 19), -- Contato com 2 emails
(23, 'fabio.correia@example.com', 20),
(24, 'fabio.correia2@example.com', 20); -- Contato com 2 emails

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


