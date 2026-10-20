#Escribe una función es_mayor_de_edad(edad) que reciba una edad y regrese True si es mayor o igual a 18, o False si no. Pruébala con 2 edades distintas.
def es_mayor_de_edad (edad):
    if edad>=18:
        return True
    else:
        return False
    

resultado= es_mayor_de_edad(18)
print(resultado)