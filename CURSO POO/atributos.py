class Celular:
    #Atributos de instancia
    #metodo constructor o funcion constructora
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"estas haciendo una llamada desde un {self.modelo}")

    def cortar(self):
        print(f"cortaste la llamada desde un {self.modelo} ")    

   
celular1= Celular("samsung", "s26", "48mp")
celular2= Celular("google", "pixel 10", "48mp")
celular3= Celular("apple", "18 pro", "48mp")

celular3.llamar()
celular3.cortar()

