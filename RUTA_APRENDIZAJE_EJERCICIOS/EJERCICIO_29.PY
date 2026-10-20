#**(reto)** ☕ Dada la lista de precios del menú, calcula cuántos productos puede pedir un cliente con un presupuesto dado (ej. $150), sin pasarse del presupuesto, recorriendo el menú y acumulando.
#- *Pista:* usa una variable acumulador `total_gastado = 0` y un contador `productos_comprados = 0`. En cada vuelta pregunta si sumar el siguiente precio se pasa del presupuesto; si no, súmalo y aumenta el contador.

productos_a_vender=[25,40,53,60,70,75,68,20]
ingresa_presupuesto =int(input("ingresa el presupuesto que tienes: "))
total_gastado=0
productos_comprados=0
for producto in productos_a_vender:
    if total_gastado + producto <= ingresa_presupuesto:
        total_gastado += producto
        productos_comprados += 1
    
print(f"gastaste: {total_gastado}")
print(f"llevas {productos_comprados} productos comprados")