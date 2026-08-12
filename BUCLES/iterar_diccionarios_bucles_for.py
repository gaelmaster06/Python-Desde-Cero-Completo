diccionario = {
    "nombre" : 'modo',
    "apellido": 'ingeniero',
    "subs": 500000
    }
#recorriendo diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key=datos[0]
    value=datos[1]
    print(f'la clave es: {key} y el valor es: {value}')

#otra forma de recorrer diccionarios mas efectiva es
for key,value in diccionario.items():
    print(f'la clave es: {key} y el valor es: {value}')


