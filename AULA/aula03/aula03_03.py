
'''

---------------------------------------------------------------------------------------------------------------------------------
biblioteca = datetime
---------------------------------------------------------------------------------------------------------------------------------

# funionalidade de hora e dia
# to importando 
import datetime

# vou bota a funcionalidade na variavel data_atual = datetime vai junto do datetime e com agora.
data_atual = datetime.datetime.now()

# vai inprimir(ano, mes, dia, hora, minutos, segundos e milisegundos)
print (data_atual)

print (data_atual.day)#vai ser indicado o dia
print (data_atual.hour)#vai ser indicado a hora
print (data_atual.month)#vai ser indicado a mes
print (data_atual.year())#vai ser indicado ano
....etc
---------------------------------------------------------------------------------------------------------------------------------

import datetime

data_atual = datetime.datetime.now()

if data_atual.hour >= 6 and data_atual.hour < 12:
    print("Bom dia")
elif data_atual.hour >= 12 and data_atual.hour < 18:
    print("Boa tarde")
else:
    print("boa noite")
    
---------------------------------------------------------------------------------------------------------------------------------
nova biblioteca = math
---------------------------------------------------------------------------------------------------------------------------------

import math

print(math.sqrt(25))#raiz quadrada
print(math.pow(5))#potencia

---------------------------------------------------------------------------------------------------------------------------------
nova biblioteca = random
---------------------------------------------------------------------------------------------------------------------------------


# vai me da numero aleatorio de forma randomica
import random

numero = random.randint(1,4)

print(numero)

---------------------------------------------------------------------------------------------------------------------------------
import random

numero = random.randint(0,10)

numeroUser = int(input("Me de um numero entre (0 e 100): "))

---------------------------------------------------------------------------------------------------------------------------------

import random

numero = random.randint(0,10)

numeroUser = int(input("Me de um numero entre (0 e 100): "))

if numero == numeroUser:
    print("voce ganhou")
else:
    print("voce perdeu")
    
print(f"o numero gerado foi {numero}")#quando quiser junta texto e variavel o 'f' e necessario para permitir o uso de variavel no print ou em texto
    
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------

'''

