j = 0
n = 0
for i in range(10):
    num = int(input(f'Digite o {i+1} numero: '))
    
    if num > 0:
        j+=1
    else:
        n+=1
        
print(f'A quantidade de numero positivo: {j}')
print(f'A quantidade de numero negativo: {n}')