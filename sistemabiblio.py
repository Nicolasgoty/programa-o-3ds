# Definição da classe Livro
class Livro:
    # Método construtor que inicializa os atributos do livro
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo  # Define o título do livro
        self.autor = autor  # Define o autor do livro
        self.paginas = paginas  # Define o número de páginas do livro

    # Método especial que retorna o número de páginas do livro ao usar a função len()
    def __len__(self):
        return self.paginas  # Retorna o número total de páginas

    # Método especial que retorna representação textual do livro ao usar a função str()
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"  # Retorna uma descrição formatada do livro

    # Método especial que compara dois objetos da classe Livro para verificar se são iguais
    def __eq__(self, outro):
        return self.titulo == outro.titulo and self.autor == outro.autor  # Retorna True se o título e autor forem iguais

# Cria dois objetos da classe Livro
livro1 = Livro("Python para Todos", "John Doe", 300)
livro2 = Livro("Python para Todos", "John Doe", 300)

# Exibe o número de páginas do primeiro livro
print(f"O livro '{livro1.titulo}' possui {len(livro1)} páginas.")  # Saída: O livro 'Python para Todos' possui 300 páginas.

# Exibe a representação textual do primeiro livro
print(f"Descrição do livro: {livro1}")  # Saída: Descrição do livro: 'Python para Todos' por John Doe

# Compara os dois livros e apresentando o resultado
print(f"Os livros '{livro1.titulo}' e '{livro2.titulo}' sao iguais? {'Sim' if livro1 == livro2 else 'Não'}")  # Saída: Os livros 'Python para Todos' e 'Python para Todos' são iguais? Sim
