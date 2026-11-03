class Persona:
    def __init__(self,nombre,edad):
        self._nombre= nombre
        self._edad= edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre= new_nombre

#una funcion que accede a un valor privado o muy privado de una clase

roberto = Persona("lucas", 21)

nombre=roberto.get_nombre()

print(nombre)

roberto.set_nombre("gael")
nombre=roberto.get_nombre()

print(nombre)