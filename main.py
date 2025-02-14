import random

dicionarioTemas = {
    "cores": ["vermelho", "azul", "amarelo", "verde", "roxo", "preto", "branco", "laranja", "rosa", "cinza"],
    "frutas": ["banana", "uva", "maça", "pera", "melancia", "abacaxi", "morango", "manga", "laranja", "limão"],
    "animais": ["cachorro", "gato", "papagaio", "leão", "tigre", "girafa", "elefante", "macaco", "cobra", "urso"]
}

while True:
    print("Bem vindo ao jogo da forca! \nTemas disponíveis: 1 - cores, 2 - frutas, 3 - animais, 4 - sair do jogo")
    entrada = str(input("Digite um tema da sua escolha: "))

    if entrada == "4":
        print("Obrigado por jogar! Você saiu do jogo")
        break
    elif entrada == "1":
        palavra = random.choice(dicionarioTemas["cores"])
    elif entrada == "2":
        palavra = random.choice(dicionarioTemas["frutas"])
    elif entrada == "3":
        palavra = random.choice(dicionarioTemas["animais"])

    tentativas = ["-"] * len(palavra)
    letrasErradas = []

    print("A palavra tem", len(palavra), "letras")
    print("".join(tentativas))

    for i in range(12):
        jogada = str(input("Digite uma letra: "))

        if jogada in palavra:
            for j in range(len(palavra)):
                if palavra[j] == jogada:
                    tentativas[j] = jogada
            resposta = "".join(tentativas)

            print("Forca: " + resposta + " Chances restantes: " + str(12 - i))

            if resposta == palavra:
                print("Parabéns, você acertou a palavra! A palavra é " + resposta + "!")
                break

        else:
            letrasErradas += [jogada]
            resposta = "".join(tentativas)
            print("Forca: " + resposta + " Chances restantes: " + str(12 - i))
            letrasJaUsadas = " ".join(letrasErradas)
            print("A letra " + jogada + " não está na palavra\nLetras erradas já digitadas: " + letrasJaUsadas)

    else:
        print("Você perdeu! Forca!")
