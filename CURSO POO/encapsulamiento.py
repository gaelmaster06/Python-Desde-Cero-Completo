class MiClase:

    def __init__(self):
        #atributo privado "_"
        self.__atributo_privado = "valor"
        #atributo muy privado "__"
objeto = MiClase()
print(objeto.__atributo_privado)