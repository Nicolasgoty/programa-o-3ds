import sqlite3

# =========================
# BANCO DE DADOS
# =========================

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


# =========================
# FUNÇÃO CADASTRAR CLIENTE
# =========================

def cadastrar_cliente():
    print("\n===== CADASTRO DE CLIENTE =====")

    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()

    # Validação
    if nome == "" or email == "" or telefone == "":
        print("\n⚠️ ATENÇÃO: Todos os campos devem ser preenchidos!")
        return

    cursor.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (?, ?, ?)
    """, (nome, email, telefone))

    conexao.commit()

    print("\n✅ Cliente cadastrado com sucesso!")


# =========================
# FUNÇÃO LISTAR CLIENTES
# =========================

def listar_clientes():
    print("\n===== CLIENTES CADASTRADOS =====")

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
E-mail: {cliente[2]}
Telefone: {cliente[3]}
-----------------------------""")


# =========================
# FUNÇÃO LIMPAR FORMULÁRIO
# =========================

def limpar_formulario():
    print("\n🧹 Formulário limpo com sucesso!")


# =========================
# MENU PRINCIPAL
# =========================

while True:
    print("""
==============================
     CADASTRO DE CLIENTES
==============================

1 - Cadastrar cliente
2 - Listar clientes
3 - Limpar formulário
4 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        limpar_formulario()

    elif opcao == "4":
        print("\nPrograma encerrado.")
        break

    else:
        print("\n⚠️ Opção inválida!")

conexao.close()


# Inicia o programa
janela.mainloop()
