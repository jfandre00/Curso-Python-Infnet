-- Criar a tabela Livro
CREATE TABLE Livro (
id_livro INT PRIMARY KEY AUTOINCREMENT NOT NULL,
isbn TEXT NOT NULL,
titulo TEXT NOT NULL,
genero TEXT NOT NULL,
data_publicacao TEXT NOT NULL,
qte_paginas INTEGER NOT NULL,
num_exemplares INTEGER NOT NULL,
);

-- Criar a tabela Autor
CREATE TABLE Autor (
id_autor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome TEXT NOT NULL,
pais_origem TEXT NOT NULL
);

-- Criar a tabela Usuario
CREATE TABLE Usuario (
id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome TEXT NOT NULL,
sobrenome TEXT NOT NULL,
data_nascimento TEXT NOT NULL
);

-- Criar a tabela Emprestimo
CREATE TABLE Emprestimo (
id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
id_usuario INTEGER NOT NULL,
data_emprestimo TEXT NOT NULL,
data_devolucao TEXT,
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Criar a tabela Livro_Autor (associação entre Livro e Autor)
CREATE TABLE Livro_Autor (
id_livro INTEGER NOT NULL,
id_autor INTEGER NOT NULL,
PRIMARY KEY (id_livro, id_autor),
FOREIGN KEY (id_livro) REFERENCES Livro(id_livro),
FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);

-- Criar a tabela Emprestimo_Livro (associação entre Emprestimo e Livro)
CREATE TABLE Emprestimo_Livro (
id_emprestimo INTEGER NOT NULL,
id_livro TEXT NOT NULL,
PRIMARY KEY (id_emprestimo, id_livro),
FOREIGN KEY (id_emprestimo) REFERENCES Emprestimo(id_emprestimo),
FOREIGN KEY (id_livro) REFERENCES Livro(id_livro)
);
