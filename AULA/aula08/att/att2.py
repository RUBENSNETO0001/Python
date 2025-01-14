with open('AULA/aula08/att2Texto.txt', 'r') as arquivo:
    for i in arquivo:
        print(len(arquivo.readlines()) + 1)