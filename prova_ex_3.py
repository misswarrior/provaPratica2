def retornaMatriz(linhas, colunas):
    listaLinhas = [0]*linhas
    matriz = listaLinhas * colunas
    return matriz

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = retornaMatriz(linhas, colunas)

contaImpar = 0
menorValor = 0

for line in range(linhas):
    for column in range(colunas):
        matriz[line][column] = int(input("Digite um número: "))
        valor = matriz[line][column]

        if valor < menorValor or (line == 0 and column == 0):
            menorValor = valor

        if valor % 2 == 0:
            contaImpar += 1

for linha in matriz:
    print(linha)

print("A matriz tem: " + str(contaImpar) + " valores impares")
print("O menor valor é " + str(menorValor))