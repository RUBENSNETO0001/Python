class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    def mostrarDAdos(self):
        print('\n\n[======================================]')
        print(f'\tNome do produto: {self.nome}')
        print('[======================================]')
        print(f'\tQuantidade do produto: {self.quantidade}')
        print(f'\tPreço do produto: {self.preco}')
        print('[======================================]')

listaProduto = []
print('[======================================]')
qtd = int(input('Quantidade de produtos a ser colocado: '))
print('[======================================]')
for i in range(qtd):
    print('\n[======================================]')
    variavel01 = input("Nome do produto: ").strip()
    variavel02 = int(input("Quantidade do produto: "))
    variavel03 = float(input("preco do produto: "))
    print('\n[======================================]')
     # variavel para colocar no produto
    produto = Produto(variavel01, variavel02, variavel03)
    listaProduto.append(produto)

for produto in listaProduto:
    produto.mostrarDAdos()