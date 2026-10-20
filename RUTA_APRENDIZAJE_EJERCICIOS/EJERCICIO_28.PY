# Dada una lista con los precios de todos los productos vendidos en un turno (ej. `[35, 40, 35, 60, 22]`), suma el total del turno usando un `for` (sin usar `sum()` todavía, para que practiques el acumulador a mano).
productos_vendidos=[25,40,53,60,70,75,68,20]
total=0
for cantidad in productos_vendidos:
    total+=cantidad

print(f"la cantidad de productos es: {total}")
