class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    def exibir_dados(self):
        print(f"O nome do Aluno é {self.nome}")
        print(f"O idade do Aluno é {self.idade}")
        print(f"O curso do Aluno é {self.curso}")

aluno1 = Aluno("Ruren", 19, "Sistema para Internet")

aluno1.exibir_dados()