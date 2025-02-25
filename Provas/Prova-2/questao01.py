class contaBacaria():
    def __init__(self, titular, cpf, conta, agencia, saldo):
        self.titular = titular
        self.cpf = cpf
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo
    
    def mostrar_dados(self):
        print("\n\nConta")
        print(f'Titulo da conta: {self.titular}')
        print(f'CPF da conta: {self.cpf}')
        print(f'conta: {self.conta}')
        print(f'Agencia da conta: {self.agencia}')
        print(f'Saldo da conta: {self.saldo:.2f}')
 # saldo - colocar       
    def Saldo(self):
        self.saldo += saldo
        
titulo = int(input('Me informe o titulo: '))
cpf = int(input('Me informe o cpf: '))
conta = int(input('Me informe a conta: '))
agencia = int(input('Me informe a agencia: '))
saldo = float(input("Deseja colocar quanto na conta: "))
conta = contaBacaria(titulo, cpf, conta, agencia, saldo)
conta.mostrar_dados()

# sacar - retirar
print('\n\nRetirar')
sacar = float(input("Deseja sacar quanto na conta: "))
      
saldo = saldo - sacar
                
conta = contaBacaria(titulo, cpf, conta, agencia, saldo)
conta.mostrar_dados()

# contaPoupança
class contaPoupanca(contaBacaria):
    def __init__(self, titular, cpf, conta, agencia, saldo, taxa_redimento):
        super().__init__(titular, cpf, conta, agencia, saldo)
        self.redimento = taxa_redimento
        
    def mostrar_dados01(self):
        print("\n\nConta Poupança")
        print(f'Titulo da conta: {self.titular}')
        print(f'CPF da conta: {self.cpf}')
        print(f'conta: {self.conta}')
        print(f'Agencia da conta: {self.agencia}')
        print(f'Saldo da conta: {self.saldo:.2f}')
        print(f'Saldo da conta com taxa de rendimento: {self.redimento:.2f}')
    

taxa_redimento = (saldo * 0.5) + saldo

contapoupanca = contaPoupanca(titulo, cpf, conta, agencia, saldo, taxa_redimento)
contapoupanca.mostrar_dados01()