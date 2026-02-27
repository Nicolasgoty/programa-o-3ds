# Solicita o preço do produto
preco_original = float(input("Digite o preço do produto: R$ "))

# Solicita o código de desconto (A, B ou C)
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Define as porcentagens de desconto (exemplo: A=10%, B=20%, C=30%)
if codigo == "A":
    desconto = 0.10  # 10%
    print("Desconto de 10% aplicado.")
elif codigo == "B":
    desconto = 0.20  # 20%
    print("Desconto de 20% aplicado.")
elif codigo == "C":
    desconto = 0.30  # 30%
    print("Desconto de 30% aplicado.")
else:
    desconto = 0
    print("Código inválido. Nenhum desconto aplicado.")

# Calcula o preço final
valor_desconto = preco_original * desconto
preco_final = preco_original - valor_desconto

# Exibe o resultado formatado
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final a pagar: R$ {preco_final:.2f}")
