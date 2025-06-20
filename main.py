import sqlite3
from datetime import datetime
import gui
import db

# ---------------------- BANCO DE DADOS ----------------------

def conectar():
    return sqlite3.connect("biblioteca.db")

# ---------------------- LIVROS ----------------------

class Livro:
    def __init__(self):
        pass

    def adicionar(self, dados, label):
        try:
            con = db.conectar()
            cur = con.cursor()
            cur.execute('''
                INSERT INTO Livro (titulo, autor, ano_publicacao, genero, quantidade)
                VALUES (?, ?, ?, ?, ?)
            ''', (dados["titulo"], dados["autor"], int(dados["ano"]), dados["genero"], int(dados["quantidade"])))
            con.commit()
            con.close()
            label.config(text="Livro adicionado com sucesso!", fg="green")
        except Exception as e:
            label.config(text=f"Erro: {e}", fg="red")

    def listar(self):
        con = db.conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM Livro")
        dados = cur.fetchall()
        con.close()
        return dados


# ---------------------- USUÁRIOS ----------------------

class Usuario:
    def __init__(self):
        pass

    def cadastrar(self, dados, label):
        try:
            con = db.conectar()
            cur = con.cursor()
            cur.execute('''
                INSERT INTO Usuario (nome, cpf, endereco, telefone, email)
                VALUES (?, ?, ?, ?, ?)
            ''', (dados["nome"], dados["cpf"], dados["endereco"], dados["telefone"], dados["email"]))
            con.commit()
            con.close()
            label.config(text="Usuário cadastrado com sucesso!", fg="green")
        except Exception as e:
            label.config(text=f"Erro: {e}", fg="red")

    def listar(self):
        con = db.conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM Usuario")
        dados = cur.fetchall()
        con.close()
        return dados


# ---------------------- EMPRÉSTIMOS ----------------------

class Emprestimo:
    def __init__(self):
        pass

    def registrar(self, dados, label):
        try:
            data_emprestimo = datetime.now().strftime("%Y-%m-%d")
            data_prevista = datetime.strptime(dados["data_prevista"], "%d-%m-%Y").strftime("%Y-%m-%d")

            if data_prevista < data_emprestimo:
                label.config(text="Data inválida.", fg="red")
                return

            con = db.conectar()
            cur = con.cursor()

            # Verifica usuário
            cur.execute("SELECT * FROM Usuario WHERE id = ?", (dados["id_usuario"],))
            usuario = cur.fetchone()
            if not usuario:
                label.config(text="Usuário não encontrado.", fg="red")
                return

            # Verifica livro
            cur.execute("SELECT quantidade FROM Livro WHERE id = ?", (dados["id_livro"],))
            livro = cur.fetchone()

            if not livro:
                label.config(text="Livro não encontrado.", fg="red")
                return
            elif livro[0] <= 0:
                label.config(text="Livro indisponível.", fg="red")
                return

            # Registrar empréstimo
            cur.execute('''
                INSERT INTO Emprestimo (id_usuario, id_livro, data_emprestimo, data_prevista, data_devolucao)
                VALUES (?, ?, ?, ?, ?)
            ''', (dados["id_usuario"], dados["id_livro"], data_emprestimo, data_prevista, None))

            # Atualiza estoque
            cur.execute("UPDATE Livro SET quantidade = quantidade - 1 WHERE id = ?", (dados["id_livro"],))

            con.commit()
            con.close()
            label.config(text="Empréstimo registrado com sucesso!", fg="green")

        except Exception as e:
            label.config(text=f"Erro: {e}", fg="red")

    def listar(self):
        con = db.conectar()
        cur = con.cursor()
        cur.execute('''
            SELECT 
                e.id,
                u.nome,
                l.titulo,
                e.data_emprestimo,
                e.data_prevista,
                e.data_devolucao
            FROM Emprestimo e
            JOIN Usuario u ON e.id_usuario = u.id
            JOIN Livro l ON e.id_livro = l.id
        ''')
        dados = cur.fetchall()
        con.close()
        return dados

    def devolver(self, dados, label):
        try:
            data_devolucao = datetime.now().strftime("%Y-%m-%d")

            con = db.conectar()
            cur = con.cursor()

            cur.execute("SELECT id_livro, data_devolucao FROM Emprestimo WHERE id = ?", (dados["id_emprestimo"],))
            emprestimo = cur.fetchone()

            if not emprestimo:
                label.config(text="Empréstimo não encontrado.", fg="red")
                return

            id_livro, devolvido = emprestimo

            if devolvido:
                label.config(text="Este livro já foi devolvido.", fg="orange")
                return

            # Atualiza devolução
            cur.execute("UPDATE Emprestimo SET data_devolucao = ? WHERE id = ?", (data_devolucao, dados["id_emprestimo"]))
            cur.execute("UPDATE Livro SET quantidade = quantidade + 1 WHERE id = ?", (id_livro,))

            con.commit()
            con.close()
            label.config(text="Livro devolvido com sucesso!", fg="green")

        except Exception as e:
            label.config(text=f"Erro: {e}", fg="red")


# ---------------------- AGRUPADOR DO SISTEMA ----------------------

class Sistema:
    def __init__(self):
        self.livro = Livro()
        self.usuario = Usuario()
        self.emprestimo = Emprestimo()

# ---------------------- INICIAR INTERFACE E SISTEMA ----------------------

if __name__ == "__main__":
    db.criar_tabelas()
    
    sistema = Sistema()
    gui.MenuPrincipal(sistema).iniciar() #inicia a interface (abre as janelas com as funcionalidades)
