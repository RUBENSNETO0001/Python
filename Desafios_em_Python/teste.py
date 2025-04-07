saldo = 1100
        
while True:
    entrada = int(input('Menu do Banco:\n1 - ver saldo\n2 - Adicionar\n3 - Retirar\n4 - Sair:\n\n'))

    if entrada == 1: 
        print(f"Saldo: {saldo}")
        
    elif entrada == 2:
        qtdcolocar = float(input('Me informe Qanto vai ser adicionado no saldo: '))
        saldo += qtdcolocar
        print(f"Saldo: {saldo}")
        
    elif entrada == 3: 
        qtdRetirar = float(input('Me informe quanto vai ser retirado'))
        saldo -+ qtdRetirar
        print(f"Saldo: {saldo}")
    elif entrada == 4: 
        print("Saindo do Banco digital")
        break
    else:
        print("Error com comando, Função não encontrada!!")