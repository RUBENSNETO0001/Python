'''
aula passada
for variavel in range(101):
    print(f"Contagem : {variavel}")
    
---------------------------------------------------

senha = ""
while senha != "1234":
    senha = int(input('Digite aqui a senha: '))
print('Deu bom')

------------------------------------------------------
Aula 05 - lista
------------------------------------------------------

lista_animes = ['naruto', 'dragon ball Z', 'nanatsu no taizai']

print(type(lista_animes))

for i in lista_animes:
    print(i)
    
-----------------------------------------------------------------------------------------

lista_animes = ['naruto', 'dragon ball Z', 'nanatsu no taizai']

# tentar fazer a lista com um tipo de variavel so.

lista_variavel = [3, 'txt', 3.3, True, '+ text']

print(type(lista_animes))
print(type(lista_variavel))

for i in lista_animes:
    print(i)

-----------------------------------------------------------------------------------------

array = [1, 2, 3, 4, 5, 6]

print(array[4])

-----------------------------------------------------------------------------------------

lista = ['naruto', 'dragon ball Z', 'nanatsu no taizai']

print(lista[2])
print(lista[0:2])

for i in lista[1]:
    print(i)

-----------------------------------------------------------------------------------------

lista = ['naruto', 'dragon ball Z', 'nanatsu no taizai']

lista[1] = ["Muito Bom"]
print(lista)

-----------------------------------------------------------------------------------------

lista = ['naruto', 'dragon ball Z', 'nanatsu no taizai']

for i in range(len(lista)):
    print(f'indice {i}: {lista[i]}')

-----------------------------------------------------------------------------------------

listadecompras = ['maça', 'banana', 'melancia']

listadecompras.append("mamão")
print(listadecompras)

-----------------------------------------------------------------------------------------

listadecompras = ['maça', 'banana', 'melancia']

# Adicionar no final da lista
listadecompras.append("mamão")

# colocar em qualquer canto da lista
listadecompras.insert(0,'pipino')

print(listadecompras)
-----------------------------------------------------------------------------------------

listadecompras = ['maça', 'banana', 'melancia']

#eliminar o ultimo elemento
listadecompras.pop()
#remover oque foi escrito
listadecompras.remove("maça")

print(listadecompras)

-----------------------------------------------------------------------------------------

listadecompras = ['maça', 'banana', 'melancia']

#ordenar em ordem alfabetica
listadecompras.sort()
# faz em prdem inversa a lista
listadecompras.reverse()
# para mostar o tamanho ta lista
print(len(listadecompras))

print(listadecompras)

-----------------------------------------------------------------------------------------

#tuple(lista que não vao muda)
listadecompras = ["azul", "rosa"]

-----------------------------------------------------------------------------------------

numero = {1, 2 ,2 , 3, 4 , 5}

print(numero)

-----------------------------------------------------------------------------------------

#estrutura de dicionario
aluno = {
    'nome': "joao",
    'nascimento': 23,
    'peso': 100
}
#se eu quiser so o nome, posso fazer com todo o indice ai por exemplo o peso e so colocar o 'peso'
print(aluno['nome'])

-----------------------------------------------------------------------------------------

#estrutura de dicionario
aluno = {
    'nome': "joao",
    'nascimento': 23,
    'peso': 100
}

#se eu quiser so o nome, posso fazer com todo o indice ai por exemplo o peso e so colocar o 'peso'
print(aluno['nome'])
# alterar
aluno['nome'] = "julio"

print(aluno)
# todas as chaves do dicionario
print(aluno.keys())

#remover
aluno.pop('nascimento')
print(aluno)

'''
