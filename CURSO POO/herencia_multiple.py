
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.name = nombre
        self.age = edad
        self.nationality = nacionalidad
    def hablar(self):
        print("hola, estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.hability=habilidad

    def mostrar_habilidad(self):
        print(f"mi habilidad es: {self.hability}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self, habilidad)
        self.salary=salario
        self.interprise=empresa
    def presentarse(self):
        return f"{super().mostrar_habilidad()}"




Roberto = EmpleadoArtista("Roberto", 22, "mexicano","Aprender", "400000", "foxxcon" )

Roberto.presentarse()
