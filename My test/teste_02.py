j = 0
n = 0
x = 0
for i in range(10):
    num = int(input(f'Digite o {i+1} numero: '))
    
    if num > 0:
        j+=1
    elif num < 0:
        n+=1
    else:
        x+=1
        
        
print(f'A quantidade de numero positivo: {j}')
print(f'A quantidade de numero negativo: {n}')
print(f'A quantidade de numero neutros: {x}')