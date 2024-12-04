nomeVendedor = input()
salarioFixo = float(input())
produtosVendidos = float(input())

print(f'TOTAL = R$ {salarioFixo+produtosVendidos*0.15 :.2f}')