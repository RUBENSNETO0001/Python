class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_salario_anual(self):
        salarioAtual = self.salario * 12
        print(f"Nome do funcionario: {self.nome}\nSalario: {salarioAtual:.2f}")
        
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus ):
        super().__init__(nome, salario)
        self.bonus = bonus
    def calcular_salario_anual(self):
        salario_gerente = (self.salario + (self.salario * self.bonus)) * 12
        print(f"Nome do funcionario: {self.nome}\nSalario do Gerente:{salario_gerente:.2f}")

class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao
        
    def calcular_salario_anual(self):
        salario_vendedor = self.salario + (self.salario * self.comissao) * 12
        print(f"Nome do Vendedor: {self.nome}\nSalario do Gerente:{salario_vendedor:.2f}")

print("\n")
salario = Funcionario('João', 1400)
salario.calcular_salario_anual()
print("\n")
salario2 = Gerente('Kleber', 1400, 0.15)
salario2.calcular_salario_anual()
print("\n")
salario3 = Vendedor('Juliano', 1400, 0.5)
salario3.calcular_salario_anual()