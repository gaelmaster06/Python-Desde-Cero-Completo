#creando una lista con list()
lista = list(["hola", "estoy", "modo-ingeniero", "modo dios", "1"])
#print(lista)

cadena = "hola, estoy, modo-ingeniero, modo dios"
cantidad_elementos = len(lista) #len es una funcion que nos permite saber la longitud de una lista, es decir, cuantas elementos tiene una lista
#print(resultado)

#agregando elementos a una lista con append()
lista.append("modo crack") #append es un metodo que nos permite agregar un elemento al final de una lista
#print(lista)

#agregando un elemento a la lista en un indice especifico
lista.insert(0,"que pasa crack") #insert es un metodo que nos permite agregar un elemento a una lista en un indice especifico, el primer parametro es el indice y el segundo parametro es el elemento que queremos agregar
#print(lista)

#extend agrega varios elementos a una lista, recibe como parametro otra lista
#agregando varios elementos a una lista con extend()
lista.extend(["primer parametro", "modo bestia", "ingeniero"])
#print(lista)

#eliminando un elemento de la lista(por su indice) con pop()
lista.pop(0) #pop es un metodo que nos permite eliminar un elemento de una lista, en este caso se elimina que pasa crack
lista.pop(-1)#para eliminar el ultimo elemento de la lista se puede usar el indice -1
#print(lista)

#removiendo un elemento de la lista(por su valor) con remove()
lista.remove("primer parametro") #remove es un metodo que nos permite eliminar un elemento de una lista, en este caso se elimina el primer parametro
#print(lista)

#eliminando todos los elementos de la lista con clear()
#lista.clear() #clear es un metodo que nos permite eliminar todos los elementos de una lista

#sort ordena los elementos de una lista, si son numeros los ordena de menor a mayor, si son cadenas los ordena alfabeticamente
lista.sort() #sort es un metodo que nos permite ordenar los elementos de una lista, en este caso se ordena alfabeticamente
#lista.sort(reverse=True) si usamos el parametro reverse=True lo ordena al reves ['modo-ingeniero', 'modo dios', 'modo crack', 'modo bestia', 'hola', 'estoy']
#print(lista)

#invirtiendo los elementos de una lista con reverse
lista.reverse()
print(lista)

#verificando si un elemente se encuentra en la lista, es importante ponerlo en '' o " "
#y te arroja el indice
#sino se encuentra marca un error
buscando_elemento = lista.index('1')
print(buscando_elemento)

