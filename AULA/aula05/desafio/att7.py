i_1 = 0  # Contador de contatos

# Lista para armazenar os contatos
contato = []

# MENU
menu = ''
while menu != 0:
    print('\tOpção da Agenda Telefônica')
    print('\n(1) Adicionar contato')
    print('(2) Buscar contato')
    print('(3) Exibir todos os contatos')
    print('(0) Sair dos contatos')
    menu = int(input('Digite o número da opção: '))
    
    # Adicionar contato
    if menu == 1:
        print('\n\n\nOpção (Adicionar contato):')
        nome = input('Me informe o nome do contato: ')
        numero = input('Me informe o número: ')
        
        # Adicionando o contato como um dicionário na lista 'contato'
        contato.append({'nome': nome, 'numero': numero})
        
        i_1 += 1  # Incrementa a quantidade de contatos
        print('\n\nContatos:')
        print(f'Quantidade de contatos: {i_1}')
        print('\nLista de contatos:')
        for c in contato:
            print(f"Nome: {c['nome']}\nNúmero: {c['numero']}")
    
    # Buscar um contato
    elif menu == 2:
        encontrado = False
        print('\n\n\nOpção (Buscar contato):')
        buscar = input('Digite o nome do contato: ')
        
        # Buscar o contato na lista de dicionários
        for c in contato:
            if c['nome'].lower() == buscar.lower():  # Comparação sem diferenciar maiúsculas/minúsculas
                print('\n\nContato encontrado:')
                print(f"Nome: {c['nome']}")
                print(f"Número: {c['numero']}")
                encontrado = True
                break
        # senão encontrar
        if not encontrado:
            print('Esse contato não existe na lista.')
            
    #concertar aqui tbm
    elif menu == 3:
        print('\n\n\nOpção (Remover contato):')
        remover = input('Numero do ')
        
        for c in contato:
                del c[1]
                
            print('Contato removido!!')
            print('\n\nContatos:')
            print(f"Nome: {c['nome']}")
            print(f"Número: {c['numero']}")
            
else:
    print('Porfavor coloque uma das opções!!')
        
# fim do programa
print("Programa finalizado!!")
