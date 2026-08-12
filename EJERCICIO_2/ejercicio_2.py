#falto el profe y los alumnos van armar la clase
#pedir el nombre y la edad de los compañeros que vinieron hoy  a clase


#funcion para obtener al asistente y al profesor segun la edad
#en esta lista se guarda el nombre y la edad de los compañeros
#ordenados segun la edad de menor a mayor
#por lo tanto el asistente sera el primer elemento y el profesor el ultimo
def obtener_compañeros(cantidad_de_compañeros):
    #creamos una lista vacia para guardar el nombre y la edad de los compañeros
    compañeros =[]
    # ejecutamos un for para pedir el nombre y la edad de los compañeros
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese el nombre del compañero:')
        edad = int(input('ingrese la edad del compañero'))
        #guardamos el nombre y la edad de los compañeros en una lista
        compañero = (nombre, edad)
        #agregando la informacion a la lista
        compañeros.append(compañero)
        #ordenamos la lista de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])
    #compañeros[x] devuelve una tupla con nombre y edad y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #retornamos una tupla 
    return asistente, profesor
#desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(5)
#imprimimos el resultado
print(f'el profesor es: {profesor} y el asistente es: {asistente}')