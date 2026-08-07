diccionario = {
    "nombre" : 'modo',
    "apellido": 'ingeniero',
    "subs": 500000
    }
#keys devuelve las claves
#keys tambien nos sirve para iterar
#claves = diccionario.keys()
#print(claves)

#devuelve un valor de lo que estes buscando en este caso de nombre, devuelve el valor de modo si no encuentre un valor no marca error sino que parece 'none'
#obtiene un elemento con get sino no encuentra nada el programa continua
#claves = diccionario.get("nombre")
#print(claves)

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop('nombre')
#print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

    
    
