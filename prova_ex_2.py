import random
dado = [1, 2, 3, 4, 5, 6]
player1 = []
player2 = []
jogadas = 0

print("Jogada Player 1")
while(input("1 - Começar / 2 - Encerrar: ")) != "2":
    if jogadas % 2 == 0:
        player1.append(random.choice(dado))
        print("Jogada player 2")
    else:
        player2.append(random.choice(dado))
        print("Jogada player 1")

    jogadas += 1

if player1:
    print("resultados: ")
    print("Jogadas player 1: " + str(player1))
    print("Jogadas player 2 : " + str(player2))
    print("Soma player 1: " + str(sum(player1)))
    print("Soma player 2: " + str(sum(player2)))

if sum(player1) > sum(player2):
    print("Player 1 é o vencedor!")
else:
    print("Player 2 é o vencedor!")