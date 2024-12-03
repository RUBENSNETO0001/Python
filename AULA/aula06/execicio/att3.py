num1 = int(input('Me informe um numero: '))

def imparouPar(num1):
    resultado = num1 % 2
    if resultado == 0:
        print('Seu numero é par')
    else:
        print("Seu nuemro e impar")
        
imparouPar(num1)