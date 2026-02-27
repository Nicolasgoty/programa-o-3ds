# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo
if numero > 0:
    # Se for positivo, imprime a mensagem
    print("O número é positivo!!.")
# Verifica se o número é negativo
elif numero < 0:
    # Se for negativo, imprime a mensagem
    print("Este número é negativo, não aceito na sociedade!")
# Se não for positivo nem negativo, é zero
else:
    # Imprime a mensagem para zero
    print("Seu número é o zero e não é considerado um número inteiro!")

