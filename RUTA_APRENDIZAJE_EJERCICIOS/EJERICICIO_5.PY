#Crea un diccionario que represente un producto de tu menú (nombre, precio, categoría: "bebida"/"alimento") e imprime cada valor usando las llaves. Esta va a ser la "forma base" que usarás después para TODO tu menú.
diccionario ={
    "nombre": 'latte de crema irlandesa' ,
    "precio": 68 ,
    "categoria": 'bebida'

}

print(f'nombre:{diccionario["nombre"]},Precio: {diccionario["precio"]}, Categoría: {diccionario["categoria"]}')

print(diccionario.keys())

print(diccionario.values())

print(diccionario.items())