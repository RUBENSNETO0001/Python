nota = float(input(f"Digite a nota(1): "))
nota2 = float(input(f"Digite a nota(2): "))
nota3 = float(input(f"Digite a nota(3): "))
nota4 = float(input(f"Digite a nota(4): "))

notaFinal = (nota+ nota2+ nota3+ nota4) / 4

print(f'{notaFinal}')

if notaFinal < 7:
    print(f'Aluno reprovado, nota: {notaFinal} ')
else:
    print(f'Aluno aprovado, nota: {notaFinal}')