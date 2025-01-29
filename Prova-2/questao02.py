class Funcionario:
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salarioBase = salario_base
        
    def mostrar_dados(self):
        print("\n\n")
        print(f"Nome do Funcionario: {self.nome}")
        print(f"cpf do Funcionario: {self.cpf}")
        print(f"salario do Funcionario: {self.salarioBase:.2f}")

funcio = Funcionario('Joao', 1212121212, 1400)
funcio.mostrar_dados()

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.bonus = bonus
        
    def mostrar_dados(self):
        print("\n\n")
        print(f"Nome do Gerente: {self.nome}")
        print(f"cpf do Gerente: {self.cpf}")
        print(f"salario do Grente: {self.salarioBase:.2f}")
        print(f"Salario do gerente mais bonus: {self.bonus}")
bonus = ((0.15 * 1400)+ 1400)
gerente = Gerente('ricardo', 122221312, 1400,bonus)
gerente.mostrar_dados()

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario_base, comissao):
        super().__init__(nome, cpf, salario_base)
        self.comissao = comissao
        
    def mostrar_dados(self):
        print("\n\n")
        print(f"Nome do Vendedor: {self.nome}")
        print(f"cpf do vendedor : {self.cpf}")
        print(f"salario do  vendedor: {self.salarioBase:.2f}")
        print(f"Salario do  vendedor mais comissao: {self.comissao}")
comissao = ((0.05 * 1400)+1400)
vedendor = Vendedor('juju', 122221312, 1400, comissao)
vedendor.mostrar_dados()