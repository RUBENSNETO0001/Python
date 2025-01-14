with open('AULA/aula08/Frase', 'x') as arquivo:
    for i in range(4):
        frase = input("Me de 3 frases: ")
        arquivo.write(f"\nfrase\n")
    print(arquivo.read())