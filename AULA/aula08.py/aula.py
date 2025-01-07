# aqui vamos manipular o arquivo
# para manipular vamos usar o open()

# r = read leitura
# w = write Escrita
# a = append adicionar
# x = criar arquivos
'''
# abrir arquivo 
arquivo = open('linguagem.txt', 'r')

# funções
# se permite leitura
print(arquivo.readable())

# para ler
print(arquivo.read())

# quebra de linha
print(arquivo.readline())

# transforma cada linha em um item de lista
lista = arquivo.readlines())
print(lista (1))

# adiconar no arquivo
arquivo.write("\nsql\n")

# vai criar pagina nova
arquivo = open('minha_chibata.txt', 'x')

# fecha arquivo tem que fecha sempre antes de mexer em outro arquivo
arquivo.close()

# para não precisar do arquivo.close()
with open("linguagem.txt", "r") as arquivo:
    print(arquivo.read())

# error de exeção
try:
    with open("este4.txt", "x") as arquivo:
        arquivo.write("\npica\n")
except FileExistsError:
    print("arquivo ta ecxistindo")

'''
