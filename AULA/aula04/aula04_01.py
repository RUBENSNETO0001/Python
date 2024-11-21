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

-----------------------------------------------------------------------------------------------------------------------------------

pi = 3.141573485
print(f'O valor de pi arrendondado é {pi:3f}')#com frestring
print(f'O valor de pi arrendondado é', round(pi,3))#sem frestring

-----------------------------------------------------------------------------------------------------------------------------------

# for
for i in range(1,101):
    print(f'Numero: {i}')


-----------------------------------------------------------------------------------------------------------------------------------

# for com string
name = "rubens"
for letra in nome:
    print(letra)

-----------------------------------------------------------------------------------------------------------------------------------

# for lista
frutas = ['banana', 'maça', 'abacaixi']
for item in frutas:
    print(item)

-----------------------------------------------------------------------------------------------------------------------------------

# for contador

contador = 5

while contador > 0:
    print("Contado: ", contador)
    contador -= 1 #mesma coisa que (contador = contador - 1)
    
-----------------------------------------------------------------------------------------------------------------------------------

senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")
print("Acesso liberado!!")

-----------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 11):
    if i == 5:
        break #para o programa
    print(i)
    
-----------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 11):
    if i == 5:
       continue # vai ignorar o 5 e continuar
    print(i)
    
-----------------------------------------------------------------------------------------------------------------------------------
'''
