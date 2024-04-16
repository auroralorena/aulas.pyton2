print("*******************************")
print("Bem vindo ao Jogo de Advinhação")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}". format(rodada,total_de_tentativas))
    chute_string = input("Digite o seu número: ")
    print("Vocé digitou: ", chute_string)

    chute = int(chute_string)
    acertou = numero_secreto  == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Vocé acertou!")
    else:
        if(maior):
            print("Vocé errou! O seu chute foi maior que o numero secreto")
        elif(menor):
             print("Vocé errou! O seu chute foi menor que o numero secreto")
            
        rodada = rodada + 1    
 
print("Fim de Jogo")