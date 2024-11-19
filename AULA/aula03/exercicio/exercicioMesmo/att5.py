# Escreva um programa que verifica se um número é par ou ímpar.


num1 = int(input('Me de um numero: '))

resultado = num1 % 2

if resultado == 0:
    print('É par')
else:
    print('É impar')