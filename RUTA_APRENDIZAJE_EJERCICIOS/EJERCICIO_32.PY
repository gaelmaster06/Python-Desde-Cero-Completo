#Practica con `len()`, `sum()`, `max()`, `min()`, `sorted()`, `enumerate()` sobre una lista de ventas del día (montos de cada ticket): muestra la venta más alta, la más baja, el promedio del día y la lista ordenada de mayor a menor.

venta_dia=[32,68,57,45,53,20,20,20,78,98,56]

lista_ordenada= sorted(venta_dia, reverse=True)
minimo=min(venta_dia)
maximo=max(venta_dia)
promedio=sum(venta_dia)/len(venta_dia)

print(maximo)
print(minimo)
print(lista_ordenada)
print(f'{promedio:.2f}')

for posicion, venta in enumerate(venta_dia, start=1):#para esto se usa enumerate en este ejemplo sirve para recorrer una lista y obtener, al mismo tiempo, el índice/posición de cada elemento junto con su valor
    print(f'Venta #{posicion}: ${venta}')
    