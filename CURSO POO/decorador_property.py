class Persona:
    def __init__(self,nombre,edad):
        self.__nombre= nombre
        self._edad= edad

    @property
    def get_nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre=new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


roberto = Persona("roberto", 21)

nombre=roberto.nombre

print(nombre)

roberto.nombre="gael"

nombre= roberto.nombre
print(nombre)

del roberto.nombre

print("que haces maquina, se vienen cositas")

