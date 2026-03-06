import random  # Importa o módulo random para gerar números aleatórios

# Função principal do jogo
def jogar():
    # Gera um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)
    
    # Inicializa o contador de tentativas
    tentativas = 0
    
    # Define o número máximo de tentativas
    max_tentativas = 5

    # Mensagens iniciais para o jogador
    print("\n🎯 Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 10.")
    print(f"Você tem {max_tentativas} tentativas.\n")

    # Loop principal do jogo
    while tentativas < max_tentativas:
        try:
            # Captura o palpite do usuário e converte para inteiro
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("⚠️ Entrada inválida! Digite apenas números.")
            continue  # Volta para o início do loop sem contar tentativa

        # Incrementa o número de tentativas
        tentativas += 1

        # Verifica se o palpite está correto
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break  # Encerra o loop se acertar
        elif palpite < numero_secreto:
            print("🔼 Quase lá! Tente um número maior.")
        else:
            print("🔽 Quase lá! Tente um número menor.")

        # Informa quantas tentativas restam
        if tentativas < max_tentativas:
            print(f"Você ainda tem {max_tentativas - tentativas} tentativa(s).\n")

    # Caso o jogador não acerte dentro do limite de tentativas
    else:
        print(f"❌ Infelizmente, você não acertou. O número era {numero_secreto}.")
        print("Fim do jogo!")

# Função para permitir jogar novamente
def main():
    while True:
        jogar()  # Executa o jogo
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta != 's':  # Se não digitar 's', encerra
            print("👋 Obrigado por jogar! Até a próxima.")
            break

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
