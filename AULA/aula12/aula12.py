class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    def mostrarDAdos(self):
        print('\n\n2[======================================]')
        print(f'\tNome do produto: {self.nome}')
        print('[======================================]')
        print(f'Qunatidade do produto: {self.quantidade}')
        print(f'Preço do produto: {self.preco}')
        print('[======================================]')

listaProduto = []
qtd = int(input('Quantidade de produtos a ser colocado: '))

for i in range(qtd):
    variavel01 = input("Nome do produto: ").strip()
    variavel02 = int(input("Quantidade do produto: "))
    variavel03 = float(input("preco do produto: "))

     # variavel para colocar no produto
    produto = Produto(variavel01, variavel02, variavel03)
    listaProduto.append(produto)

for produto in listaProduto:
    produto.mostrarDAdos()