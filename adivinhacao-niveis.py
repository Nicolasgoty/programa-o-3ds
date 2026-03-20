import random

def jogar():
    print("--- Bem-vindo ao Jogo de Adivinhação Nível Pro! ---")
    
    # Configurações de dificuldade
    niveis = {
        "facil": 10,
        "medio": 50,
        "dificil": 100
    }
    
    escolha = ""
    while escolha not in niveis:
        escolha = input("Escolha a dificuldade (Fácil, Médio, Difícil): ").strip().lower()
        if escolha not in niveis:
            print("Opção inválida! Por favor, digite 'Fácil', 'Médio' ou 'Difícil'.")

    # Define o limite máximo baseado na escolha
    limite_maximo = niveis[escolha]
    numero_secreto = random.randint(1, limite_maximo)
    max_tentativas = 7  # Você pode ajustar isso ou tornar dinâmico também
    
    print(f"\nVocê escolheu o modo {escolha.capitalize()}.")
    print(f"Tente adivinhar o número entre 1 e {limite_maximo}. Você tem {max_tentativas} tentativas.")

    for tentativa in range(1, max_tentativas + 1):
        try:
            palpite = int(input(f"\nTentativa {tentativa}/{max_tentativas}. Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros!")
            continue

        if palpite == numero_secreto:
            print(f"🎯 Parabéns! Você acertou em {tentativa} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Mais alto... Tente um número maior.")
        else:
            print("Mais baixo... Tente um número menor.")

        if tentativa == max_tentativas:
            print(f"\nSinto muito, suas tentativas acabaram. O número era {numero_secreto}.")

    print("\n--- Fim do jogo! ---")

if __name__ == "__main__":
    jogar()
