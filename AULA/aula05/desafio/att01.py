array = []

for i in range(5):
    num = int(input('Digite os numeros aqui: '))
    array.append (num)
   
print(f'Maior numero: {max(array)}')
print(f'Menor numero: {min(array)}')
print(f'Soma numero: {sum(array)}')