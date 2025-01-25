class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.estoque = 0
        
    def detalhes(self):
        print(f"Nome do Produto {self.nome}")
        print(f"Preço do Produto {self.preco}")
        print(f"Quantidade do Produto {self.estoque}")
        
    def saldinho(self):
        self.estoque += 1
        return self.estoque
produto = Produto("ivone", 45.23)

novo_estoque = produto.saldinho()

produto.detalhes()