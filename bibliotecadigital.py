class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método especial para retornar a representação em texto do objeto
    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"


# --- Programa Principal ---
print("--- Cadastro de Livro - Biblioteca Digital ---")

# Solicitando os dados ao usuário
titulo_input = input("Digite o título do livro: ")
autor_input = input("Digite o autor do livro: ")

# Tratamento simples para garantir que o número de páginas seja um número inteiro
try:
    paginas_input = int(input("Digite a quantidade de páginas: "))
except ValueError:
    print("Valor inválido para páginas. Definindo como 0.")
    paginas_input = 0

print("\n--- Verificação de Dados ---")

# Criando a instância (objeto) da classe Livro
novo_livro = Livro(titulo_input, autor_input, paginas_input)

# Exibindo a descrição formatada (o Python chama o método __str__ automaticamente aqui)
print(novo_livro)
