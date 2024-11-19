# Crie um programa que solicite um número aleatório, e verifique se esse numero escolhido bate com o numero gerado aleatoriamente (utilize a função Random)


import random

numero = random.randint(0,10)

numeroUser = int(input("Me de um numero entre (0 e 100): "))

if numero == numeroUser:
    print("voce ganhou")
else:
    print("voce perdeu")
    
print(f"o numero gerado foi {numero}")#quando quiser junta texto e variavel o 'f' e necessario para permitir o uso de variavel no print ou em texto
    