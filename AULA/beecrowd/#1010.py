x = input().split()
y = input().split()

xtotal = int(x[1])* float(x[2])
ytotal = int(y[1])* float(y[2])

result = xtotal + ytotal

print(f'VALOR A PAGAR: R$ {result:.2f}')