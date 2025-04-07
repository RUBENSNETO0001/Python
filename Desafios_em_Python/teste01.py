numero = float(input('Adicione um numero: '))

def Calculadora(numero):
    for i in range(11):
        resposta = numero * i
        if i >= 1:
            print(f'multiplicação: {resposta}')

Calculadora(numero)