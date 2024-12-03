def mediaNotas(nota1, nota2, nota3, nota4):
    #resultado = (nota1 + nota2 + nota3 + nota4) / 4
    
    nota = nota1, nota2 , nota3 ,nota4

    resultado = sum(nota) / len(nota)
    if resultado:
        print(f'A media das notas é {resultado}')

nota1 = int(input('Me de a nota do primeiro bimestre'))
nota2 = int(input('Me de a nota do segundo bimestre'))
nota3 = int(input('Me de a nota do terceiro bimestre'))
nota4 = int(input('Me de a nota do quarto bimestre'))

mediaNotas(nota1, nota2, nota3, nota4)