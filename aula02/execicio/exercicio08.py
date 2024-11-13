valorProduto = int(input('Me informe o valor do produto: '))

pagamento = int(input('Pagamento: '))

if pagamento > valorProduto:
    resultado = pagamento - valorProduto
    print('O troco é', resultado)
else:
    print('O pagamento é abaixo ao valor do produto')