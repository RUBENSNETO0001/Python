'''

# aqui vamos criar o objeto Pessoa
class Pessoa:
    # vamos da as suas caractericas que mais vai se repetir como nome e idade
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
    # aqui vou fazer uma apresentação que um metedo ou fução
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
# vou joga os dados em uma variavel
pessoa1 = Pessoa("Joao", 30)
# e mostar na tela
pessoa1.apresentar() # print(f"Olá, meu nome é joao e tenho 30 anos")

==============================================================================================

class Carro:
    def __init__(self, marcaDoCarro, cor, modelo):
        self.marcaDoCarro = marcaDoCarro
        self.cor = cor
        self.modelo = modelo
    # isso aqui se torna uma função = metedo
    def apresentacao(self):
        print(f"A marca do carro é {self.marcaDoCarro} da cor {self.cor} e o modelo é {self.modelo} ")

carro = Carro('chiba', 'amarelo', 12222)
carro.apresentacao()

==============================================================================================

class Cachorro:
    def __init__(self, nome , idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def documentacao(self):
        print(f"Nome do animal: {self.nome}")
        print(f"idade do animal: {self.idade}")
        print(f"sexo do animal: {self.sexo}")

animalzinho = []

for i in range(2):
    print("\n\nDocumento\n\n")
    animal = input("Me informe o nome do animal: ")
    animalIdade = int(input("Me informe a idade: "))
    animalsexo = input("Me informe o sexo do animal: ")
    
    cachorrinho = Cachorro(animal,animalIdade,animalsexo)
    animalzinho.append(cachorrinho)

print("============================================================================")
for cachorrinho in animalzinho:
    print("\n\nDocumentação\n")
    cachorrinho.documentacao()

==============================================================================================
# metodo especial, para inicializar o objeto
__init__

==============================================================================================

class ContaBanco:
    def __init__(self, Titulo , N_conta, N_agencia):
        self.titulo = Titulo
        self.NConta = N_conta
        self.Nagencia = N_agencia
        self.saldo = 0
    def documentacao(self):
        print(f"Titulo: {self.titulo}")
        print(f"Numero da conta: {self.NConta}")
        print(f"Numero da agencia: {self.Nagencia}")
        print(f"saldo: {self.saldo}")
conta = []

for i in range(2):
    print("\n\nBanco\n\n")
    titulo = int(input("Me informe o Titulo: "))
    num_conta = int(input("Me informe o numero da conta: "))
    num_agencia = int(input("Me informe o numero da agencia: "))
    
    conta_infot = ContaBanco(titulo,num_conta,num_agencia)
    conta.append(conta_infot)

print("============================================================================")
for conta_infot in conta:
    print("\n\nDocumentação\n")
    conta_infot.documentacao()
    
escolhaSaldo = input("\n\nQue colocar saldo em alguma conta: ")

if escolhaSaldo == 's' or escolhaSaldo =='si' or escolhaSaldo =='sim':
    conta_posi = int(input("Quanto conta a ser colocado o saldo: "))
    
    for i in conta_posi:
        if i == conta_infot:
            try:
                saldo = float(input("Me informe o valor: "))
                conta[i] = saldo
            except ValueError:
                print("Error")

print("============================================================================")
for conta_infot in conta:
    print("\n\nDocumentação\n")
    conta_infot.documentacao()
    
escolhaSaldo = input("\n\nQue colocar saldo em alguma conta: ")

escolhacontar_retirar = input("\n\nQue sacar saldo em alguma conta: ")
if escolhacontar_retirar == 's' or escolhacontar_retirar =='si' or escolhacontar_retirar =='sim':
    conta_posi = int(input("Quanto conta a ser retirado o saldo: "))
    
    for i in conta_posi:
            if i == conta_infot:
                try:
                    saldo = float(input("Me informe o valor: "))
                    conta[i] -= saldo
                    print(f"O valor retirado foi {saldo} e a conta tem atualmente {conta[i]}")
                except ValueError:
                    print("Error")
==============================================================================================

class contabancaria:
    def __init__(self, titular, Conta, Agencia):
        self.titular = titular
        self.Conta = Conta
        self.Agencia = Agencia
        self.Saldo = 0  
    
    def mostrar(self):
        print("_" * 25, "\n")
        print(f'Número da conta: {self.Conta}')
        print(f'Número da agência: {self.Agencia}')
        print(f'Titular da conta: {self.titular}')
        print(f'Saldo da conta: R${self.Saldo}') 
        print("_" * 25, "\n")

    def deposito(self, valor):
        #self.Saldo = self.Saldo + valor #Outra forma de fazer
        self.Saldo += valor
        print(f"Foi depositado R${valor} na conta do titular {self.titular}")

    def saque(self, valor):
        if valor > self.Saldo:
            print("Saldo insuficiente para o saque!!")
        else:
            self.Saldo-=valor
        print(f'Foi sacado {valor} na conta do titular {self.titular}')


# Criando uma conta e exibindo os detalhes
Banco = contabancaria('Sarah Lavyne', 224848, 2136)
Banco.mostrar()

Banco.deposito(150)
Banco.mostrar()
Banco.deposito(90)
Banco.mostrar()
Banco.saque(45)
Banco.mostrar()

==============================================================================================

# herança

class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def mover(self):
        print(f"O veiculo {self.tipo} ta se movendo")

veiculo1 = Veiculo("moto")
veiculo1.mover()

==============================================================================================

# herança

class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def mover(self):
        print(f"O veiculo {self.tipo} ta se movendo")

class Carro(Veiculo):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo
        
veiculo1 = Veiculo("moto")
veiculo1.mover()

veiculo2 = Carro ('carro', 'fiat')
veiculo2.mover()

==============================================================================================

# polimofismo

class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def mover(self):
        print(f"O veiculo {self.tipo} ta se movendo")

class Carro(Veiculo):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo
        
    def mover(self):
        print(f"O veiculo {self.tipo} e modelo {self.modelo} ta se movendo")   
        
veiculo1 = Veiculo("moto")
veiculo1.mover()

veiculo2 = Carro ('carro', 'fiat')
veiculo2.mover()

==============================================================================================

==============================================================================================

==============================================================================================
'''
# polimofismo

class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def mover(self):
        print(f"O veiculo {self.tipo} ta se movendo")

class Carro(Veiculo):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo
        
    def mover(self):
        print(f"O veiculo {self.tipo} e modelo {self.modelo} ta se movendo")   
        
veiculo1 = Veiculo("moto")
veiculo1.mover()

veiculo2 = Carro ('carro', 'fiat')
veiculo2.mover()