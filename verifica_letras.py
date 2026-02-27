# Solicita letra ao usuário e converte em minúscula
letra = input("Digite uma letra: ").lower()

# Verifica se a letra é uma vogal
if letra in "aeiou":
    # Se for vogal, imprime "Vogal."
    print("Vogal.")
else:
    # Se não for vogal, imprime "Consoante."
    print("Consoante.")
