# Solicita o peso do usuário em kg
peso = float(input("Digite o peso em kg: "))

# Solicita a altura do usuário em metros
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC (Índice de Massa Corporal)
# A fórmula é: imc = peso / altura²
imc = peso / (altura ** 2)

# Exibe o valor do IMC formatado com duas casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Classifica o IMC e exibe a mensagem
if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")
