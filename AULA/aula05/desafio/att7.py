i_1 = 0 # e so um contador mesmo
# ARMAZENAR O CONTATO
contato = []
chave = {
    'chave': 'nome'
}
numero = {
    'valor': 'numero'
}
# ARMAZENAR O CONTATO

# MENU
menu = ''
# TAVA PENSANDO
while menu != 0:
    print('\tOpcão da agenda Telefônica')
    print('\n(1) Adicionar contato')
    print('(2) Buscar contato')
    print('(3) Adicionar contato')
    
    menu = int(input('Digite aqui o numero da opção: '))
    
    if menu == 1:
        print('\n\n\nOpção (Adicionar contato):')
        chave = input('Me informe o nome do contato: ')
        numero = input('Me informe o numero: ')
        
        contato.append(chave)
        contato.append(numero)
        
        i_1 += 1
        print('\n\nContatos:')
        print('Quantidade de numeros(', i_1,'):')
        print('\n')
        for i in range(len(contato)):
            print(contato[i])
                
    # rever essa escolha, concertar
    elif menu == 2:
        print('\n\n\nOpção (Buscar contato):')
        buscar = input('Digite o nome do contato: ')
        
        for i in range(len(chave)):
            if chave == buscar:
                local = len(chave)
            
                print('\n\nContato:')
                print(chave[local])
                print(numero[local])
                             
        else:
            print('Esse contato não existe na lista')
    #concertar aqui tbm
    elif menu == 3:
        print('\n\n\nOpção (Remover contato):')
        remover = input('Digite o nome do contato: ')
        
        contato.Remover(remover)
        
        i_1 += 1
        print('\n\nContatos:')
        print('Quantidade de numeros(', i_1,'):')
        for i in range(len(contato)):
            print(contato[i])
            if i > len(contato):
                print('-------------------')
    else:
        print('Porfavor coloque uma das opções!!')
