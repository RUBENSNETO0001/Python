# para mim, como e uma funçaõ pequena não precisa ter 4 funções para cada uma, claro que pode mais na minha opniao nao e necessario
def calculadoraSimples(num1, num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    
    if num1 == 0 or num2 == 0:
        print('Não tem como dividir se tiver zero')
    else:
        print(num1/num2)

num1 = int(input('Me de um numero: '))
num2 = int(input('Me de um numero: '))

calculadoraSimples(num1, num2)