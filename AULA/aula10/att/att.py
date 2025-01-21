from matplotlib import pyplot as gp

gp.style.use('dark_background')
eixoX_meses = [1,2,3,4,5,6,7,8,9,10,11,12]
eixoY_venda = [13,41,53,63,23,25,45,23,12,23]

gp.plot(eixoX_meses, marker = 'o', color = 'r')
gp.plot(eixoY_venda, marker = '^', color = 'b')

gp.title("Tabela de vendas")
gp.xlabel("Meses")
gp.ylabel("Vendas")

gp.legend(['Produto A','Produto A'])

gp.grid(True)

gp.show()