numeros = []
for i in range(5):
    num = int(input('Digite numeros: '))
    numeros.append(num)
print(numeros)
num02 = int(input('Me de um numero para remover:'))

if  num02 in numeros  :
    numeros.remove(num02) 
    print(numeros)
else:
    print('Esse numero não ta aqui')