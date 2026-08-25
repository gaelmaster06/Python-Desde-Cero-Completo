#Crea un diccionario donde cada valor sea otra lista, representando las ventas de la semana por producto (ej. `{"Café Americano": [12, 15, 10], "Muffin": [5, 8, 6]}`). Calcula el promedio de ventas diarias de cada producto.
diccionario={"cafe_americano": [12,15,20], "muffin": [10,30,5]}

prom_cafe_americano= sum(diccionario["cafe_americano"]) /len(diccionario["cafe_americano"])
prom_muffins= sum(diccionario["muffin"]) /len(diccionario["muffin"])
print(f'el promedio de venta de cafe americano es: {prom_cafe_americano:.2f}')
print(f'el promedio de venta de muffin es: {prom_muffins}')

