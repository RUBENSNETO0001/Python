class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_detalhes(self):
        print(f"A marca do veiculo é {self.marca}")
        print(f"O modelo do veiculo é {self.modelo}")
        print(f"O ano do veiculo é {self.ano}")
    
veiculo1 = Veiculo('Nissan', 'GTR Skyline R34', 1998)

veiculo1.exibir_detalhes()

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_combustivel):
        super().__init__(marca, modelo, ano)
        self.tipo_combustivel = tipo_combustivel
    def exibir_detalhes(self):
        print(f"O tipo do combostivel é {self.tipo_combustivel}")
        
veiculo2 = Carro('Nissan', 'GTR Skyline R34', 1998, "Gasolina")
veiculo2.exibir_detalhes()

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def exibir_detalhes(self):
        print(f"O quantidade de cilindradas é{self.cilindradas}")

veiculo3 = Carro('honda', 'CG', 2015, "Gasolina", '15')
veiculo3.exibir_detalhes()