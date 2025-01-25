class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def calcular_salario_anual(self):
        self.salario * 12
        
class Gerente(Funcionario(Funcionario)):
    def __init__(self, bonus):
        self.bonus = bonus
    def calcular_salario_anual(self):
        self.calcular_salario_anual + self.bonus
        
class Vendedor(Funcionario):
    def __init__(self, comissao):
        self.comissao = comissao
    def comissao_bonus(self):
        self.comissao = self.salario + 15