# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


num1 = int(input('Me de um numero: '))

if num1 > 0:
    print(f"O numero {num1} é positivo.")
elif num1 < 0:
    print(f"O numero {num1} é negativo.")
else:
     print("O numero é 0.")