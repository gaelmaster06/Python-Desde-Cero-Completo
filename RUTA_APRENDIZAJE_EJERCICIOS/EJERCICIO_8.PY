#Pide el stock actual de vasos y el stock mínimo permitido; muestra si el stock actual es mayor, menor o igual al mínimo (solo con expresiones booleanas, sin `if` todavía). Esta comparación es la base de una futura "alerta de reabastecimiento" en tu POS.

stock = int(input("cuantos vasos hay en inventario: "))
stock_minimo = int(input("cual es el inventario minimo requerido: "))

stock_es_menor = stock < stock_minimo 
print(f'{stock_es_menor} el stock de los vasos es menor al minimo')
stock_es_igual = stock == stock_minimo
print(f'{stock_es_igual} el stock de los vasos es igual al minimo')
stock_es_mayor = stock > stock_minimo 
print(f'{stock_es_mayor} el stock de los vasos es mayor al stock minimo')

print(f' el stock actual es:  {stock}')


 





