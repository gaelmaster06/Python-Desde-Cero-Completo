#**(reto)** ☕ Simula la validación de una promoción "2x1 en café": debe cumplirse que el cliente pida al menos 2 cafés **y** que sea antes de las 12:00, **o** que sea miércoles (día de la promo fija) sin importar la hora.
# - *Pista:* primero arma la condición de "antes de las 12 y al menos 2 cafés" combinando con `and`. Luego únela con `or` a la condición del miércoles.
cantidad_cafes = int(input('ingresa la cantidad de cafes que ordenaras: '))
hora= int(input('ingresa la hora: '))
es_miercoles = input('hoy es miercoles? (si/no) ').lower() == "si"

promocion = (cantidad_cafes >= 2 and hora<12 ) or es_miercoles
print(f'tienes promocion de 2X1 en cafes?: {promocion}') 
