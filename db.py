import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")


def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER,
        genero TEXT,
        quantidade INTEGER
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE,
        endereco TEXT,
        telefone TEXT,
        email TEXT UNIQUE
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Emprestimo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_livro INTEGER,
        data_emprestimo TEXT,
        data_prevista TEXT,
        data_devolucao TEXT,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
        FOREIGN KEY (id_livro) REFERENCES Livro(id)
    )
    ''')

    con.commit()
    con.close()
