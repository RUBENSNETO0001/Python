with open('att2Texto.txt', 'r') as arquivo:
    for i in arquivo:
        print(len(arquivo.readlines()) + 1)