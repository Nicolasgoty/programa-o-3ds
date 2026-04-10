# Passo 1: Recebe o número de elementos (n)
n = int(input("Digite a quantidade de números (n): "))

# Inicializa uma lista vazia
lista_numeros = []

# Passo 2: Lê n números e os adiciona à lista
print(f"Digite os {n} números:")
for i in range(n):
    num = int(input())
    lista_numeros.append(num)

# Passo 3: Recebe o número x para busca
x = int(input("Digite o número que deseja encontrar (x): "))

# Passo 4: Verifica se x pertence à lista
if x in lista_numeros:
    print(f"O número {x} pertence à lista.")
else:
    print(f"O número {x} não pertence à lista.")
