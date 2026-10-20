
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.name = nombre
        self.age = edad
        self.nationality = nacionalidad
    def hablar(self):
        print("hola, estoy hablando un poco")
#herencia simple
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.work=trabajo
        self.salary=salario



empleado = Empleado("Roberto", 22, "mexicano","ing mecatronico", "18000")


print(f"""""
    Datos del empleado: \n\n
    nombre: {empleado.name} \n
    Edad: {empleado.age}\n
    Nacionalidad: {empleado.nationality}\n
    Trabajo: {empleado.work}\n
    Salario: {empleado.salary}\n
"""""
)
empleado.hablar()