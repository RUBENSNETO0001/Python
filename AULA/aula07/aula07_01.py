'''

<aula passada>
# def = função
def soma(num1, num2):
    print(num1+num2)
# função de processamento, do executa algum
soma(5,9)
soma(2,2)
soma(8,8)

def somaComReturn(num1,num2):
    return num1+num2

# não vai imprimir na tela a soma, mais posso colocar em uma variavel e imprimir na tela
somaComReturn(4,2)

somaa = somaComReturn(4,2)

print(somaa)
============================================================================================
<aula 7>

# como acessar o index a posissão

filme = ['harry potter','Crepusculo']
print(filme[1])
nome = "Rubens Neto"

print(nome[4])

============================================================================================

frase = "Não me mama mamae!! meu pau e pequeno demais para voce"

print(frase[0:11])

filme = ['harry potter','Crepusculo','transforme']
print(filme[0:2]) #indice - 1

filme = ['harry potter','Crepusculo','transforme']
print(filme[0:2:2]) #indice - 1 pula 2 em 2
print(filme[4:]) #4 em diante
print(filme[::-1]) #de trans para frente

============================================================================================

frase = "Não Me Mama Mamae!! Meu Pau e Pequeno demais para voce"

print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())

============================================================================================

frase = "Não Me Mama Mamae!! Meu Pau e Pequeno demais para voce"

print(len(frase))
print(frase.count('n')) #conta uma palavra
print(frase.find("n"))#ostra a primeira localização do que estamos a procurar

print(frase.strip())#formata o cod

print(frase.replace('Pau', 'pinto'))#trocar palavra

============================================================================================

frase = "Não Me Mama Mamae!! Meu Pau e Pequeno demais para voce"

print(frase.split())#dividir text em indice
print('-'.join())#unir text em form indice

frase2 ='-'.join(frase)#unir text em form indice
print(frase)
print(frase2)

============================================================================================

nome ='rubens'

print('nome'+ nome)

# não posso fazer isso em baixo
print('nome'+ nome+ 2)

============================================================================================v

pi = 3.14159

print(f'valor de pi{pi:.2f}')
'''

