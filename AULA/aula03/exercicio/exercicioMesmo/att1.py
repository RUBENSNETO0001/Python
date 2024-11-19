# Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input('Me de um numero: '))
num2 = int(input('Me de outo numero: '))

if num1 > num2:
    print(f'O numero {num1} e maior que o numero {num2}')
elif  num2 > num1:
    print(f'O numero {num2} e maior que o numero {num1}')
else:
    print(f'Os numeros {num1} e{num2} são numeros iguais.')