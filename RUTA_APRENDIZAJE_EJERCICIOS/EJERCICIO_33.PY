#Usa `enumerate()` para imprimir el ticket de una orden con cada producto numerado empezando en 1 (así se ve un ticket real, no como índice de lista que empieza en 0).

orden=["muffin","cafe americano","rol"]
for indice,producto in enumerate(orden, start=1):
     print(f'{indice}: {producto}')


