#Crea una función `validar_orden(carrito)` que reciba una lista de productos (diccionarios con nombre, precio, cantidad) y regrese una lista de errores encontrados (ej. `["El carrito está vacío", "Muffin tiene cantidad 0"]`). Si no hay errores, la orden está lista para cobrarse.
# - *Pista:* crea una lista vacía `errores = []` dentro de la función. Recorre el carrito con un `for` y en cada validación que falle haz `errores.append("mensaje")`. Al final, la función regresa esa lista (si está vacía, la orden es válida). Esta es exactamente la lógica de validación que usarás en las "vistas" de Django antes de guardar una orden en la base de datos.
def validar_orden(carrito):
    errores = []

    if len(carrito) == 0:
        errores.append("El carrito está vacío")

    for producto in carrito:
        if producto["cantidad"] == 0:
            errores.append(f'{producto["nombre"]} tiene cantidad 0')

    return errores


carrito_prueba = [
    {"nombre": "Muffin", "precio": 20, "cantidad": 2},
    {"nombre": "Latte frio irlandesa", "precio": 65, "cantidad": 1},
    {"nombre": "Rol canela", "precio": 53, "cantidad": 5}
]

resultado = validar_orden(carrito_prueba)
print(resultado)






  