class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print("Som genérico do animal.")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def fazer_som(self):
        super().fazer_som()
        print("Au Au!")
animal = Cachorro('cachorro')
animal.fazer_som()

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def fazer_som(self):
        super().fazer_som()
        print("Miau!")
animal = Gato('gato')
animal.fazer_som()