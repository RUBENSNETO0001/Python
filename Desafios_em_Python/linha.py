contato = []

while True:
    escolha = int(input('\n\tContato\n[1] Adicionar contato\n[2] Listar contatos\n[3] Buscar contato\n[4] Remover contato\n[5] Sair\n\n'))
    if escolha == 1:
        nome_novo = input('Me informe o nome do novo usuario: ')
        Numero_novo = input('Me informe o numero do novo usuario: ')
        contato.append({'nome': nome_novo,'numero': Numero_novo})
        print("Contato adicionado!!")
    elif  escolha == 2:
        print('\tContatos')
        for i in contato:
            print('\n==============================')
            print(f'Nome Contato: {i['nome']}')
            print(f'Numero Contato: {i['numero']}')
    elif escolha == 3:
        nome_buscar = input('\nMe informeo nome a ser buscado:(Caso nao saiba o nome so o numero digite 0)\n\n')
        if nome_buscar == '0':
            numero_buscar = int(input('Me informe o numero do contato: '))
            for c in contato:
                if numero_buscar == c['numero']:
                    print(f'Nome do Contato: {c['nome']}')
                    print(f'Numero do contato: {c['numero']}')
                    
        else:
            for c in contato:
                if nome_buscar == c['nome']:
                    print(f'Nome do Contato: {c['nome']}')
                    print(f'Numero do contato: {c['numero']}')
                else: print('contato não encontrado!!')
    elif escolha == 4:
        nome_remove = input('Me informe o nome do contato a ser removido: ')
        
        for c in contato:
            if nome_remove == c['nome']:
                contato.remove(c)
        print('Contato apagado')
    elif escolha == 5:
        print("Saindo da aplicação")
        break