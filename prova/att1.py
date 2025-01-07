idade = int(input('Digite a sua idade: '))

print(f'Você possui {idade} e então Você é: ')
if idade < 12:
    print('Criança')
elif idade >= 12 and idade <=17:
    print('Adolecente')
elif idade >= 18 and idade <=59:
    print('Adulto')
else:
    print('Idoso')