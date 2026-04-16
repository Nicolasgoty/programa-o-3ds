palavra_secreta = "girafa"
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
erros = 0

# Desenho da forca por etapas
forca = [
    """
     _______
    |       |
    |       
    |      
    |      
    |      
    |
    """,
    """
     _______
    |       |
    |       O
    |      
    |      
    |      
    |
    """,
    """
     _______
    |       |
    |       O
    |       |
    |       |
    |      
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|
    |       |
    |      
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |       |
    |      
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |       |
    |      / 
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |       |
    |      / \\
    |
    """
]

print("Bem-vindo ao Jogo da Forca!\n")

while tentativas > 0 and "_" in letras_acertadas:
    print(forca[erros])
    print("Palavra:", " ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").lower().strip()

    # Verifica se a letra já foi digitada
    if palpite in letras_acertadas:
        print("Você já acertou essa letra!")
        continue

    if palpite in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[index] = letra
        print("Acertou!")
    else:
        erros += 1
        tentativas -= 1
        print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

if "_" not in letras_acertadas:
    print("\nParabéns, você ganhou!")
    print("Palavra:", "".join(letras_acertadas))
else:
    print(forca[erros])
    print("\nQue pena, você perdeu. A palavra era:", palavra_secreta)
