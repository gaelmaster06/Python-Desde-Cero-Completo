#Crea una función `calcular_total_con_descuento(precio, cantidad, porcentaje_descuento)` que regrese el precio final de una línea de la orden. Esta función reemplaza directamente al ejercicio 11 pero ahora reutilizable.
def total_descuento(precio,cantidad,porcentaje):
    subtotal= precio*cantidad
    descuento=subtotal*porcentaje/100
    total=subtotal-descuento
    return total
ingrese_precio=float(input(f"ingrese el precio:"))
ingrese_cantidad=int(input("ingrese cuantos va a llevar:"))

if ingrese_cantidad >= 3 and ingrese_cantidad <= 5:
    porcentaje = 5
elif ingrese_cantidad >= 6 and ingrese_cantidad <= 10:
    porcentaje = 10
elif ingrese_cantidad > 10:
    porcentaje = 15
else:
    porcentaje = 0

total_final =total_descuento(ingrese_precio, ingrese_cantidad, porcentaje)
print(f'el total a pagar es: {total_final:.2f}')




