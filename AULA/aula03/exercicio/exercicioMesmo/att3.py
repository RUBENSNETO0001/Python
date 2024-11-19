# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Me de uma letra: ")

if letra == 'a' and letra == 'e' and letra == 'i' and letra == 'o' and letra == 'u' or letra == 'A' and letra == 'E' and letra == 'I' and letra == 'O' and letra == 'U':
    print('é vogal')
else:
    print('é consoante')