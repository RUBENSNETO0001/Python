nome = input('Me informe seu nome: ')
idade = int(input('Me informe a sua idade: '))
altura = float(input('Me informe a sua altura: '))

frase = f'Seu nome é {nome}, Você tem {idade} e tem {altura:.2f}'

print(frase.capitalize())