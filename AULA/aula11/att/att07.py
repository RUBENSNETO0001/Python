class Livro:
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir):
        self.matricula = matricula
        self.nome = nome
        self.qtd_pagina = qtdPagina
        self.datadelacamento = datadelancamento
        self.possuir = possuir
        
class Bibliotecario(Livro):
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao):
        super().__init__(matricula, nome, qtdPagina, datadelancamento, possuir)
        self.nome_bibliotecario = nomeDobibliotecario
        self.cpf_bibliotecario = cpf_bibliotecario  
        self.permissao = permissao
        
class Usuario(Bibliotecario, Livro):
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao, cpf_Usuario, nome_usuario):
        super().__init__(matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao)
        self.cpf_user = cpf_Usuario
        self.nome_user = nome_usuario
        
    def emprestimo(self):
        if self.permissao == True and self.possuir == True:
            print(f"\n\nNome do Bibliotecario: {self.nome_bibliotecario}\nCpf do bibliotecario: {self.cpf_bibliotecario}")
            print(f"\n\nNome do Usuario: {self.nome_user}\nCpf do Usuario: {self.cpf_user}")
            print("\n\n--------===========[O Livro foi Liberado ao Usuario]===========--------")
            print(f"\nCodigo do livro: {self.matricula}\nNome do livro: {self.nome}\nQuantidade de paginas: {self.qtd_pagina}\nData de lançamento: {self.datadelacamento}")
        # caso um dos 2 for igual a False que para termos normais seria o Não permitido
        else:
            print(f"\n\nNome do Bibliotecario: {self.nome_bibliotecario}\nCpf do bibliotecario: {self.cpf_bibliotecario}")
            print(f"\n\nNome do Usuario: {self.nome_user}\nCpf do Usuario: {self.cpf_user}")
            print("\n\n--------===========[O Livro foi Negado ao Usuario]===========--------")
            print("\nLivro não existente no estoque")

            #Usuario(matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao, cpf_Usuario, nome_usuario)
permissao = Usuario('00001','Crepusculo', 600, 2012, True, 'Jorge', 99213321224, True, 13314143332, 'Andre')
permissao.emprestimo()