# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par
if numero % 2 == 0:
    # Se for par, imprime a mensagem
    print(f"{numero} é par.")
else:
    # Se for ímpar, imprime a mensagem
    print(f"{numero} é impar!.")
