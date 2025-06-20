import tkinter as tk
from tkinter import ttk

# ---------------------- JANELA DE LIVROS ----------------------

class JanelaLivro:
    def __init__(self, sistema):
        self.sistema = sistema

    def adicionar(self):
        janela = tk.Toplevel()
        janela.title("Adicionar Livro")
        janela.geometry("400x400")

        tk.Label(janela, text="Título").place(x=20, y=20)
        titulo = tk.Entry(janela)
        titulo.place(x=150, y=20)

        tk.Label(janela, text="Autor").place(x=20, y=60)
        autor = tk.Entry(janela)
        autor.place(x=150, y=60)

        tk.Label(janela, text="Ano de Publicação").place(x=20, y=100)
        ano = tk.Entry(janela)
        ano.place(x=150, y=100)

        tk.Label(janela, text="Gênero").place(x=20, y=140)
        genero = tk.Entry(janela)
        genero.place(x=150, y=140)

        tk.Label(janela, text="Quantidade").place(x=20, y=180)
        quantidade = tk.Entry(janela)
        quantidade.place(x=150, y=180)

        resultado = tk.Label(janela, text="")
        resultado.place(x=20, y=220)

        def salvar():
            dados = {
                "titulo": titulo.get(),
                "autor": autor.get(),
                "ano": ano.get(),
                "genero": genero.get(),
                "quantidade": quantidade.get()
            }
            self.sistema.livro.adicionar(dados, resultado)

        tk.Button(janela, text="Salvar", command=salvar).place(x=150, y=260)

    def listar(self):
        janela = tk.Toplevel()
        janela.title("Lista de Livros")
        janela.geometry("700x400")

        tree = ttk.Treeview(janela, columns=("ID", "Título", "Autor", "Ano", "Gênero", "Qtd"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")
        tree.heading("Ano", text="Ano")
        tree.heading("Gênero", text="Gênero")
        tree.heading("Qtd", text="Quantidade")

        tree.column("ID", width=40)
        tree.column("Título", width=150)
        tree.column("Autor", width=120)
        tree.column("Ano", width=60)
        tree.column("Gênero", width=100)
        tree.column("Qtd", width=80)

        tree.place(x=10, y=10, width=680, height=350)

        for row in self.sistema.livro.listar():
            tree.insert("", "end", values=row)

# ---------------------- JANELA DE USUÁRIOS ----------------------

class JanelaUsuario:
    def __init__(self, sistema):
        self.sistema = sistema

    def cadastrar(self):
        janela = tk.Toplevel()
        janela.title("Cadastrar Usuário")
        janela.geometry("400x400")

        tk.Label(janela, text="Nome").place(x=20, y=20)
        nome = tk.Entry(janela)
        nome.place(x=150, y=20)

        tk.Label(janela, text="CPF").place(x=20, y=60)
        cpf = tk.Entry(janela)
        cpf.place(x=150, y=60)

        tk.Label(janela, text="Endereço").place(x=20, y=100)
        endereco = tk.Entry(janela)
        endereco.place(x=150, y=100)

        tk.Label(janela, text="Telefone").place(x=20, y=140)
        telefone = tk.Entry(janela)
        telefone.place(x=150, y=140)

        tk.Label(janela, text="Email").place(x=20, y=180)
        email = tk.Entry(janela)
        email.place(x=150, y=180)

        resultado = tk.Label(janela, text="")
        resultado.place(x=20, y=220)

        def salvar():
            dados = {
                "nome": nome.get(),
                "cpf": cpf.get(),
                "endereco": endereco.get(),
                "telefone": telefone.get(),
                "email": email.get()
            }
            self.sistema.usuario.cadastrar(dados, resultado)

        tk.Button(janela, text="Salvar", command=salvar).place(x=150, y=260)

    def listar(self):
        janela = tk.Toplevel()
        janela.title("Lista de Usuários")
        janela.geometry("800x400")

        tree = ttk.Treeview(janela, columns=("ID", "Nome", "CPF", "Endereço", "Telefone", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("CPF", text="CPF")
        tree.heading("Endereço", text="Endereço")
        tree.heading("Telefone", text="Telefone")
        tree.heading("Email", text="Email")

        tree.column("ID", width=50)
        tree.column("Nome", width=150)
        tree.column("CPF", width=150)
        tree.column("Endereço", width=120)
        tree.column("Telefone", width=120)
        tree.column("Email", width=120)
        tree.place(x=10, y=10, width=780, height=350)

        for row in self.sistema.usuario.listar():
            tree.insert("", "end", values=row)

# ---------------------- JANELA DE EMPRÉSTIMOS ----------------------

class JanelaEmprestimo:
    def __init__(self, sistema):
        self.sistema = sistema

    def registrar(self):
        janela = tk.Toplevel()
        janela.title("Registrar Empréstimo")
        janela.geometry("400x300")

        tk.Label(janela, text="ID Usuário").place(x=20, y=20)
        id_usuario = tk.Entry(janela)
        id_usuario.place(x=150, y=20)

        tk.Label(janela, text="ID Livro").place(x=20, y=60)
        id_livro = tk.Entry(janela)
        id_livro.place(x=150, y=60)

        tk.Label(janela, text="Data Prevista (DD-MM-AAAA)").place(x=20, y=100)
        data_prevista = tk.Entry(janela)
        data_prevista.place(x=150, y=130)

        resultado = tk.Label(janela, text="")
        resultado.place(x=20, y=180)

        def salvar():
            dados = {
                "id_usuario": id_usuario.get(),
                "id_livro": id_livro.get(),
                "data_prevista": data_prevista.get()
            }
            self.sistema.emprestimo.registrar(dados, resultado)

        tk.Button(janela, text="Registrar", command=salvar).place(x=150, y=220)

    def listar(self):
        janela = tk.Toplevel()
        janela.title("Lista de Empréstimos")
        janela.geometry("1020x400")

        tree = ttk.Treeview(janela, columns=("ID", "Usuário", "Livro", "Emprestado", "Previsto", "Devolvido"),
                             show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Usuário", text="Usuário")
        tree.heading("Livro", text="Livro")
        tree.heading("Emprestado", text="Data Empréstimo")
        tree.heading("Previsto", text="Data Prevista")
        tree.heading("Devolvido", text="Data Devolução")

        tree.column("ID", width=50)
        tree.column("Usuário", width=150)
        tree.column("Livro", width=150)
        tree.column("Emprestado", width=120)
        tree.column("Previsto", width=120)
        tree.column("Devolvido", width=120)

        tree.place(x=10, y=10, width=1000, height=350)

        for row in self.sistema.emprestimo.listar():
            id_emp, nome_usuario, titulo_livro, data_emp, data_prevista, data_devolucao = row

            if data_devolucao is None or data_devolucao == "":
                data_devolucao = "Pendente"

            tree.insert("", "end", values=(id_emp, nome_usuario, titulo_livro, data_emp, data_prevista, data_devolucao))

    def devolver(self):
        janela = tk.Toplevel()
        janela.title("Devolver Livro")
        janela.geometry("400x200")

        tk.Label(janela, text="ID do Empréstimo").place(x=20, y=20)
        id_emprestimo = tk.Entry(janela)
        id_emprestimo.place(x=150, y=20)

        resultado = tk.Label(janela, text="")
        resultado.place(x=20, y=100)

        def salvar():
            dados = {
                "id_emprestimo": id_emprestimo.get()
            }
            self.sistema.emprestimo.devolver(dados, resultado)

        tk.Button(janela, text="Devolver", command=salvar).place(x=150, y=60)


# ---------------------- MENU PRINCIPAL ----------------------

class MenuPrincipal:
    def __init__(self, sistema):
        self.sistema = sistema

    def iniciar(self):
        root = tk.Tk()
        root.title("Sistema de Biblioteca")
        root.geometry("500x400")
        root.configure(bg="#9ef9df")

        tk.Label(root, text="Menu da Biblioteca", bg="#9ef9df", font=("Arial", 20)).place(x=120, y=30)

        opcoes = [
            "Adicionar Livro",
            "Listar Livros",
            "Cadastrar Usuário",
            "Listar Usuários",
            "Registrar Empréstimo",
            "Listar Empréstimos",
            "Devolver Livro"
        ]

        selecionado = tk.StringVar()
        selecionado.set("Opções")

        combo = ttk.Combobox(root, values=opcoes, state="readonly", font=("Arial", 13))
        combo.set("Opções")
        combo.place(x=140, y=100)

        tk.Button(root, text="Executar", width=20, height=2, bg="#5badf6", font=("Arial", 13),
                  command=lambda: self.executar_acao(combo.get())).place(x=145, y=170)

        tk.Button(root, text="Sair", width=20, font=("Arial", 13), bg="#f96d66", command=root.quit).place(x=145, y=250)

        root.mainloop()

    def executar_acao(self, opcao):
        janela_livro = JanelaLivro(self.sistema)
        janela_usuario = JanelaUsuario(self.sistema)
        janela_emprestimo = JanelaEmprestimo(self.sistema)

        match opcao:
            case "Adicionar Livro":
                janela_livro.adicionar()
            case "Listar Livros":
                janela_livro.listar()
            case "Cadastrar Usuário":
                janela_usuario.cadastrar()
            case "Listar Usuários":
                janela_usuario.listar()
            case "Registrar Empréstimo":
                janela_emprestimo.registrar()
            case "Listar Empréstimos":
                janela_emprestimo.listar()
            case "Devolver Livro":
                janela_emprestimo.devolver()
