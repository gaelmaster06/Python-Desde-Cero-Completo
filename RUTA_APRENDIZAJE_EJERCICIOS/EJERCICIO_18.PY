#Simula el "carrito" de una orden: pide al usuario productos uno por uno con un `input()` en un `for` de 5 vueltas, y agrégalos a una lista con `.append()`. Al final muestra la lista completa (el "ticket" antes de cobrar).


lista =[]
for contador_de_numero_de_vueltas_irrelevante in range(5):
    producto = input("ingresa que desea ordenar: ")
    lista.append(producto)

print(lista)