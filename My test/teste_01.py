print("Esse programa vai pega numeros e coloca em uma matriz de n x m de tamanho indecado pelo usuario e imprimir.\n")

#definindo uma função
def criar_matriz(linhas, colunas):
    """Cria uma matriz bidimensional e a preenche com valores fornecidos pelo usuário."""
    matriz = []
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            while True:
                try:
                    valor = int(input("Me informe o número para a posição [{i},{j}]: "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("Por favor, coloque um número inteiro.")
        matriz.append(linha)
    return matriz
                
numMatrizLargura = int(input('Me informe a largura da matriz: '))
numMatrizAltura = int(input('Me informe a altura da matriz: '))

minha_matriz = criar_matriz(numMatrizLargura, numMatrizAltura)

#vou imprimir
print('matriz = [')
for linha in minha_matriz:
		print(linha)
print(' ]')