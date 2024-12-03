'''
saudação():
    print("Òla seje bem vindo")
    print("Outra mensagem")
saudação()
saudação()

def saudaçãopersonalizada(nome, idade)):
    print(f"Ola {nome}, seja , bem-vindo!")
    print(f'Vove tem {idade} anos de idade')
saudaçãopersonalizada('ana', 20)
saudaçãopersonalizada('pedro', 22)

def soma(a, b):
    print(a+b)
soma(5,7)
soma(2,4)
soma(9,9)

def subtracao(num1, num2):
    print(num1-num2)
subtracao(5, 45)

def quadrado(numero):
    return numero**2
# para ultilizar a função
resultado = quadrado(5)
print(resultado)

# sem retorno
def QuadradoSemReturn(numero):
    print(numero**2)
QuadradoSemReturn(6)


#  variavel global
x = 10

def minha_funcao():
    x = 5
    print(f'Valor da minha função{x}')
# vai proorizar a função
minha_funcao()
# vai priorizar o global
print(f'Valor fora da minha função{x}')
'''