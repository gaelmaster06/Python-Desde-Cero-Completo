
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.name = nombre
        self.age = edad
        self.nationality = nacionalidad
    def hablar(self):
        print("hola, estoy hablando un poco")
#herencia jerarquica
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.work=trabajo
        self.salary=salario
#herencia jerarquica
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,calificacion,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notes=calificacion
        self.university=universidad


Roberto = Empleado("Roberto", 22, "mexicano","ing mecatronico", "18000")

Roberto.hablar()
