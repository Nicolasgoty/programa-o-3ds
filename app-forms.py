import tkinter as tk
from tkinter import messagebox
import sqlite3


# =========================
# BANCO DE DADOS
# =========================

def conectar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    return conexao


# =========================
# SALVAR CLIENTE
# =========================

def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Verifica se todos os campos foram preenchidos
    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning(
            "Atenção",
            "Todos os campos devem ser preenchidos!"
        )
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente.\n{erro}"
        )


# =========================
# LIMPAR FORMULÁRIO
# =========================

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# =========================
# VISUALIZAR CLIENTES
# =========================

def visualizar_clientes():
    # Cria uma nova janela
    janela_clientes = tk.Toplevel(janela)
    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("650x400")
    janela_clientes.resizable(False, False)

    titulo = tk.Label(
        janela_clientes,
        text="Clientes Cadastrados",
        font=("Arial", 16, "bold")
    )
    titulo.pack(pady=15)

    # Área onde os clientes serão exibidos
    lista_clientes = tk.Listbox(
        janela_clientes,
        width=85,
        height=15
    )
    lista_clientes.pack(padx=10, pady=10)

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
            ORDER BY id
        """)

        clientes = cursor.fetchall()
        conexao.close()

        # Verifica se existem clientes cadastrados
        if not clientes:
            lista_clientes.insert(
                tk.END,
                "Nenhum cliente cadastrado."
            )
        else:
            for cliente in clientes:
                id_cliente, nome, email, telefone = cliente

                texto = (
                    f"ID: {id_cliente} | "
                    f"Nome: {nome} | "
                    f"E-mail: {email} | "
                    f"Telefone: {telefone}"
                )

                lista_clientes.insert(tk.END, texto)

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível consultar os clientes.\n{erro}"
        )


# =========================
# INTERFACE GRÁFICA
# =========================

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("450x380")
janela.resizable(False, False)

# Cria o banco de dados ao iniciar
conectar_banco().close()


# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)


# Campo Nome
label_nome = tk.Label(
    janela,
    text="Nome:"
)
label_nome.pack()

entrada_nome = tk.Entry(
    janela,
    width=40
)
entrada_nome.pack(pady=5)


# Campo E-mail
label_email = tk.Label(
    janela,
    text="E-mail:"
)
label_email.pack()

entrada_email = tk.Entry(
    janela,
    width=40
)
entrada_email.pack(pady=5)


# Campo Telefone
label_telefone = tk.Label(
    janela,
    text="Telefone:"
)
label_telefone.pack()

entrada_telefone = tk.Entry(
    janela,
    width=40
)
entrada_telefone.pack(pady=5)


# =========================
# BOTÕES
# =========================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)


# Botão Salvar
botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    width=14,
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white"
)
botao_salvar.grid(row=0, column=0, padx=5)


# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=14,
    command=limpar_formulario,
    bg="#f44336",
    fg="white"
)
botao_limpar.grid(row=0, column=1, padx=5)


# Botão Visualizar Clientes
botao_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    width=32,
    command=visualizar_clientes,
    bg="#2196F3",
    fg="white"
)
botao_visualizar.pack(pady=5)


# Inicia o programa
janela.mainloop()
