def retornaListas(tamanho):
    lista = [0]*tamanho
    menorValor = 0
    for indice in range(tamanho):
       valor = int(input("Digite um número inteiro: "))
       lista[indice] = valor
       if valor < menorValor or indice == 0:
           menorValor = valor

    print(lista)
    print(sum(lista))
    print(menorValor)
    print(list(reversed(lista)))

retornaListas(int(input("Digite o tamanho da lista: ")))









