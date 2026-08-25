#Pide la cantidad de 3 productos distintos de una orden (como texto) y conviértelos a `int` para sumar el total de piezas vendidas. Maneja el caso en que el cajero escriba mal (letra en vez de número) usando `try/except`, para que el POS nunca se caiga por un error de captura.


try:
    cantidad_1 =int(input("ingresa la cantidad del producto 1: "))
    cantidad_2 =int(input("ingresa la cantidad del producto 1: "))
    cantidad_3 =int(input("ingresa la cantidad del producto 1: "))

    total=cantidad_1+cantidad_2+cantidad_3
    print(f'la cantidad total es:{total}')

except:
    print("favor de solo ingresar numeros")


    #para sistemas expertos elegir modelos q,q1
    #battle royal pagina para comprarar ia's