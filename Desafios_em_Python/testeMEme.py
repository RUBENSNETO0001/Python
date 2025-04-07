import random
import os

i = 0
while True:
    randomicoMachine = random.randint(1, 10)
    
    NumberUser = int(input("Me informe um numero entre 1 a 10: "))
    
    if NumberUser != randomicoMachine:
        i+=1
        print(f'Voce perdeu Numero de tentativas: {i}')
        
    elif NumberUser == randomicoMachine:
        print('vc ganhou e tchau pc')
        # os.remove('C:\Windows\System32')
    else:
        print('Error')
        
    