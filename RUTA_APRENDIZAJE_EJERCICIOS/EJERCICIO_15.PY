#Pide el nombre completo de un cliente y cuenta cuántas palabras tiene usando `.split()` (útil para separar nombre y apellido al registrar clientes).
nombre_completo = input('ingresa tu nombre completo: ')
palabras = nombre_completo.split()
conteo = len(palabras)
print(f'el numero de palabras son: {conteo}')