# aula passada
'''
idade = int(input("Digite sua idade: "))

if idade >= 60:
    print('A pessoa é idosa!')
elif idade >= 18:
    print("A pessoa é maior de idade!")
else:
    print('A pessoa é menor de idade! ')
-----------------------------------------------------------------------------------------
import datetime

time = datetime.datetime.now()

print(time.hour)
----------------------------------------------------------------------------------------

'''

import datetime

time = datetime.datetime.now()

print(time.day)
print(time.hour)
print(time.minute)
#formas de concatenar no py
print(f'Ahora atual é {time.hour}:{time.minute}')#forma de concatenar
print("A hora atual é ", time.hour, ":", time.minute)#forma de concatenar

nome = "Rubens"

print('Meu nome é' + nome)#forma de concatenar

print('A aula de python é extremamente '+ 3* " muito " + 2*" legal")