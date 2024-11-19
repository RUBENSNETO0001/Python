# Crie um programa que solicita a idade de uma pessoa e imprime se ela é maior ou menor de idade


idade_01 = int(input('Digite sua idade: '))

if idade_01 >= 18 and idade_01 <= 60:
    print("Adulta.")
else:
    print('Menor de idade.')