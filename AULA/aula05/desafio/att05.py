carrinhodeCompras = []
terminar = ""

while terminar != 'n':
    compras = input('\nDigite o nome do produto:')
    carrinhodeCompras.append(compras)
    terminar = input('\nDeseja adicionar mais algum no carrinho(s ou n): ')
    
escolha = input('\n\n\nDeseja remover algum item da lista (s ou n): ')
if escolha == 's':
    terminardeRemover = ''
    remover = ''
    while terminardeRemover != 'n':
        remover = input('\n\nMe de o nome do produto: ')
        terminardeRemover = input('\n\nDeseja remover mais algum item da lista (s ou n):')
        carrinhodeCompras.remove(remover)
    # imprimir a lista
    print('Lista do carrinho:')
    for i in range(len(carrinhodeCompras)):
        print(f'°{carrinhodeCompras[i]}')
else:
    print('Lista do carrinho:')
    for i in range(len(carrinhodeCompras)):
        print(f'°{carrinhodeCompras[i]}')