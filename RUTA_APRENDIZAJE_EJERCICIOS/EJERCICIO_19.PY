#Dada una lista con los productos vendidos en todo el día (con repetidos, ej. 30 ventas), crea una lista de "productos únicos vendidos" **sin usar `set()`**. Esto es la base para luego saber cuántos productos *distintos* tiene tu menú activo.
#¿¿- *Pista:* crea una lista vacía. Recorre la original con un `for`, y antes de agregar cada producto pregunta `if producto not in lista_nueva`.
venta_dia=["rol","muffin","cafe americano","latte vainilla frio","latte vainilla caliente","rol","rol","muffin","chocolate","chai manzana","chai vainilla", "tisana frutos rojos","frappe oreo", "frappe crema irlandesa","frappe crema irlandesa","frappe crema irlandesa","frappe crema irlandesa","chocolate","chai manzana","chai vainilla","matcha","matcha","matcha","matcha","matcha","cafe americano","matcha","cafe americano","matcha","cafe americano"]
productos_unicos= []

for producto in venta_dia:
    if producto not in productos_unicos:
        productos_unicos.append(producto)
        
print(productos_unicos)
