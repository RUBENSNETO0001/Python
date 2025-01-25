class Instrumento:
    def __init__(self, nome):
        self.nome = nome
    def tocar(self):
        print(f"Tocando um som genérico.")
instrumentos = Instrumento('Instrumento')
instrumentos.tocar()
        
class Violao(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    def tocar(self):
        super().tocar()
        print("Tocando acordes no violão.")
violao = Violao('violão')
violao.tocar()

class Flauta(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    def tocar(self):
        super().tocar()
        print("Tocando uma melodia na flauta.")
flauta = Flauta('flauta')
flauta.tocar()