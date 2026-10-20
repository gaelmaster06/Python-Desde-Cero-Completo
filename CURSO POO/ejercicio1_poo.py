#crear clase
#atributos nombre, edad y grado
#metodo estudiar con el mensaje "el nombre del estudiante esta estudiando"
#crear un objeto estudiante y usar el metodo estudiar 
#se debe interactuar con el usuario(se debe pedir el nombre, edad y grado)
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.name = nombre
        self.age = edad
        self.grade = grado
    def estudiar(self):
        print("estudiando...")

nombre= input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
grado = input("ingrese el grado que cursa: ")
    
estudiante1= Estudiante(nombre,edad,grado)

print(f"""
    Datos del estudiante: \n\n
    nombre: {estudiante1.name} \n
    Edad: {estudiante1.age}\n
    Grado: {estudiante1.grade}\n

""")
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()