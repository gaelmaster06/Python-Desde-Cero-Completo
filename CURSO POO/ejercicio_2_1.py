class Aninmal:
    def comer(self):
        print("el animal es comiendo")

class Ave(Aninmal):
    def volar(self):
        print("el animal esta volando")
    
class Mamifero(Aninmal):
    def amamantar(self):
        print("el animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass
murcielago=Murcielago()
ave= Ave()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()


ave.comer()
ave.volar()

print(Murcielago.mro())