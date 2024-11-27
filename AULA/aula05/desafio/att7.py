contato = {
    'chave': 'nome',
    'valor': 'numero'
}
menu = ''

while menu != 0:
    print('\tOpcão da agenda Telefônica')
    print('\n(1) Adicionar contato')
    print('(2) Buscar contato')
    print('(3) Adicionar contato')
    
    menu = int(input('Digite aqui o numero da opção: '))
    
    if menu == 1:
        print('Opção (Adicionar contato):')
        nomeContato = input('Me informe o nome do contato: ')
        numeroContato = input('Me informe o numero: ')
        
    contato = nomeContato
    contato = numeroContato
    print(contato)
