#Pide el precio de un café y la cantidad de vasos vendidos en el día; calcula el total de venta de ese producto.
precio_cafe = int(input("ingresa el precio del latte de crema irlandesa: "))
cantidad_vendidas = int(input("ingresa la cantidad de vasos vendidos en el dia:"))

ventas_crema_irlandesa = cantidad_vendidas * precio_cafe

print(f'el dia de hoy ese producto te genero {ventas_crema_irlandesa} pesos en ventas')

