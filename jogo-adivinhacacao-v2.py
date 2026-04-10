import random

def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)

def obter_palpite_do_jogador(inicio, fim):
    return int(input(f"Digite seu palpite (entre {inicio} e {fim}): "))

def avaliar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return "acertou"
    elif palpite < numero_secreto:
        return "menor"
    else:
        return "maior"

def jogar_adivinhacao():
    inicio, fim = 1, 100
    numero_secreto = gerar_numero_aleatorio(inicio, fim)
    tentativas = 5

    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Tente adivinhar o número que estou pensando, entre {inicio} e {fim}.")

    for tentativa in range(tentativas):
        palpite = obter_palpite_do_jogador(inicio, fim)
        resultado = avaliar_palpite(palpite, numero_secreto)

        if resultado == "acertou":
            print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")
            break
        else:
            dica = "maior" if resultado == "menor" else "menor"
            print(f"Seu palpite foi {resultado} que o número secreto. Tente um número {dica}.")

    if resultado != "acertou":
        print(f"O número secreto era {numero_secreto}. Tente novamente!")

if __name__ == "__main__":
    jogar_adivinhacao()

