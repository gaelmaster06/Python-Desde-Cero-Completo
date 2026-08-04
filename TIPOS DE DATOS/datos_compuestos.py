#los tipos de datos compuestos son aquellos que pueden almacenar múltiples valores en una sola variable, como listas, tuplas, conjuntos y diccionarios. 
# #creando una lista con diferentes tipos de datos se puede modificar
lista = ["gael lopez", 21, "modo ingeniero", True, 1.72]
print(lista[0])  # imprime el primer elemento de la lista
print(lista[1])  # imprime el segundo elemento de la lista
print(lista[2])  # imprime el tercer elemento de la lista
print(lista[3])  # imprime el cuarto elemento de la lista
print(lista[4])  # imprime el quinto elemento de la lista
print(lista)
lista[0] = "juan perez"  # cambia el primer elemento de la lista
print(lista)  # imprime la lista completa con el primer elemento cambiado
#una lista es un conjunto de datos que pueden ser de diferentes tipos, como enteros, cadenas de texto, booleanos, etc.
#creando un tupla con diferentes tipos de datos, no se puede modificar
tupla = ("gael lopez", 21, "modo ingeniero", True, 1.72)
print(tupla)
# tupla[0] = "juan perez"  # esto generará un error, ya que las tuplas son inmutables

#creando un conjunto (set) con diferentes tipos de datos, no se puede modificar pero si redefinir
#en un conjunto no puede haber datos duplicados, si se intenta agregar un dato que ya existe, no se agregará
#no se puede llamar a los elementos de un conjunto por su posición, ya que no tienen un orden definido
conjunto = {"gael lopez", 21, "modo ingeniero", True, 1.72, "gael lopez"}  # el dato "gael lopez" se repetirá pero no se agregará al conjunto
conjunto = {"estoy redefinido"}
print(conjunto)

#creando un diccionario
#al igual que los conjuntos tampoco tienen un orden definido, pero a diferencia de los conjuntos, los diccionarios tienen una estructura de clave-valor, donde cada elemento del diccionario está compuesto por una clave y un valor asociado a esa clave.
diccionario ={
    'nombre': "gael lopez",
    'canal' : "modo ingeniero",
    "edad" : 21,
    'altura' : 1.72,
    'es_inteligente' : True,
}
print(diccionario)
print(diccionario['nombre'])  # imprime el valor asociado a la clave 'nombre'
