#Crea un diccionario de un producto de tu cafetería (nombre, precio, categoría, disponible: True/False) y usa `.keys()`, `.values()`, `.items()` para imprimir su contenido de 3 formas distintas.

producto={
    "nombre": "latte de crema irlandesa",
    "precio": 68,
    "categoria": "bebida con cafe",
    "disponibilidad": True
} 
llave = producto.keys()
valor = producto.values()
items = producto.items()

print(f'{llave}\n{valor}\n{items}')
