class Livro:
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir):
        self.matricula = matricula
        self.nome = nome
        self.qtd_pagina = qtdPagina
        self.datadelacamento = datadelancamento
        self.possuir = possuir
    def QtdLivro(self):
        self.possuir = True
        
class Bibliotecario(Livro):
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao):
        super().__init__(matricula, nome, qtdPagina, datadelancamento, possuir)
        self.nome_bibliotecario = nomeDobibliotecario
        self.cpf_bibliotecario = cpf_bibliotecario  
        self.permissao = permissao
        
        if self.possuir == True:
            self.permissao == True
        else:
            self.permissao == False
class Usuario(Bibliotecario, Livro):
    def __init__(self, matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao, cpf_Usuario, nome_usuario):
        super().__init__(matricula, nome, qtdPagina, datadelancamento, possuir, nomeDobibliotecario, cpf_bibliotecario, permissao)
        self.cpf_user = cpf_Usuario
        self.nome_user = nome_usuario
    def emprestimo(self):
        if  self.permissao == True and self.possuir == True:
            print(f"\n\nNome do Bibliotecario: {self.nome_bibliotecario}\nCpf do bibliotecario: {self.cpf_bibliotecario}\n")
            print(f"")