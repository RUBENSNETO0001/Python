# if (expressão logica) : 'e diferente mais ok' ops. indente o codigo porra

''' 

if 5 > 4  and 4 < 2:
    print("Isso e o certo ne")
print("memama") #o delimitador em python e a indetação por isso o segundo print aqui pareceu, ele não ta na area do if

----------------------------------------------------------------------------------------------------------------------------------

if True:
    print("Isso ta errado")
    
----------------------------------------------------------------------------------------------------------------------------------

if 5 > 4  and 4 < 2:
    print("Isso ta errado")

# seria tipo o nosso  se senão ou else if
elif 5 > 4 and 4 > 2: 
    print('isso e o certo')
    
else:
    print("Isso não e verdade")
    
print('Fim do programa')

----------------------------------------------------------------------------------------------------------------------------------

idade_01 = int(input('Digite sua idade: '))

if idade_01 >= 18:
    print("Adulto.")
else:
    print('menor de idade.')

----------------------------------------------------------------------------------------------------------------------------------

idade_01 = int(input('Digite sua idade: '))

if idade_01 >= 60:
    print("idosa.")
elif idade_01 >= 18 and idade_01 <= 60:
    print("adulto.")
else:
    print('menor de idade.')

----------------------------------------------------------------------------------------------------------------------------------
'''