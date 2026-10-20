#(el que suele costar más) Escribe una función saludar(nombre) que regrese el texto f'Hola, {nombre}'. Luego, en el código principal, usa esa función dentro de un print() directamente, sin guardar el resultado en una variable primero — es decir: print(saludar("Gael")). Fíjate cómo el resultado de la función se puede usar directamente adentro de otra función, sin pasos intermedios.
def saludar(nombre):
    saludo =f'hola {nombre}'
    return saludo

print(saludar("gael"))