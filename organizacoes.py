# 2. Método remove() em Python - remocao.py
notas = [2, 2, 3, 5] 
notas.______(2) 
print("Lista de notas atualizada:", notas)



# 4. Armazenamento de dados: Tupla x Lista em Python - tupla_lista.py
# Dados fornecidos
agencia = (10, 22, 33, 44)   # tupla, pois não muda
saldo   = [1000, 2000, 3000, 4000]  # lista, pois pode mudar

print("Agências:", agencia)
print("Saldos:", saldo)

# Teste: altere o saldo da primeira conta
saldo[0] = 1500
print("Saldo atualizado:", saldo)

# Tente alterar a agência da posição 0 (deve dar erro!)
agencia[0] = 99



# 6. Características do array em Python - array_exemplo.py 
# Importa biblioteca array
import array as arr

# Observe como o tipo do array foi definido
notas = arr.array('i', [5, 7, 8, 9])

print("Notas armazenadas:", notas)

# Teste: adicione uma nova nota
notas.append(10)
print("Notas atualizadas:", notas)






#8. Igualdade: ex. comparação de igualdade no Python - conta_corrente.py
# Define a classe da conta corrente
class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero


# Criando duas contas com o mesmo número
conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(15)


# Condições para comparação de dados
if conta_do_gui == conta_da_dani:
    print('São iguais')
else:
    print('São diferentes')




# 10. Método especial __eq__ pode ser sobrescrito dentro de uma classe
# define como objetos dessa classe devem ser comparados - metodo_eq.py
# Define a classe para contas correntes
class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero


    # Sobrescreve método __eq__ para comparar contas pelo número
    def __eq__(self, other):
        return self.numero == other.numero


# Cria duas contas
conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(15)


# Condições para comparação das variáveis
if conta_do_gui == conta_da_dani:
    print('São iguais')
else:
    print('São diferentes')



# 13. Imprime índices da lista e valores correspondentes - versão 1
# Define a lista com idades
idades = [15,87,37,45,56,32,49,37]


# Laço for percorre a lista usando índices
# imprime o índice com o valor correspondente
for i in range(len(idades)):
    print(i,idades[i])


# Imprime com função embutida do Python enumerate(  ) - versão 2
# Cria uma lista com valores de idades
idades = [15, 87, 37, 45, 56, 32, 49, 37]


# Percorre a lista com enumerate, que retorna índice e valor ao mesmo tempo
for indice, valor in enumerate(idades):
    print(indice, valor)



# 16. Calcula a media de uma lista de números - calc_media.py
def calcular_media(numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma / len(numeros)

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Chamando a função
media = calcular_media(numeros)

print(f"A média é: {media:.2f}")
