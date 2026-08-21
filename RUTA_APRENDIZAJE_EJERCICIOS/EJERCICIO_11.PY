#**(reto)** ☕ Dado el precio de un producto y la cantidad pedida en una orden, aplica un descuento tipo "combo cafetería": 5% si compra 3-5 piezas del mismo producto, 10% si compra 6-10, 15% si compra más de 10. Si compra menos de 3, sin descuento. **Este es literalmente el motor de descuentos que tu POS de Django va a necesitar.**
#- *Pista:* ordena tus `if/elif` de mayor a menor cantidad o de menor a mayor, pero sé consistente para no dejar huecos lógicos.

latte_irlandesa = 68
cantidad_pedida = int(input('ingresa la cantidad de lattes de crema irlandesa que compraste: '))

precio_sin_descuento= latte_irlandesa * cantidad_pedida
#lo comentado fue mi logica pero esta manera es mas efectiva pór que se necesita menos codigo, claude code trabajo sobre en los codiciones y no tiene que agregar tantas variables

#descuento_5= precio_sin_descuento*5/100 
#precio_final_5= precio_sin_descuento-descuento_5

#descuento_10= precio_sin_descuento*10/100
#precio_final_10= precio_sin_descuento-descuento_10

#descuento_15= precio_sin_descuento*15/100
#precio_final_15= precio_sin_descuento-descuento_15

if cantidad_pedida>=3 and cantidad_pedida <=5:
    #print(f'el total a pagar con descuento es: {precio_final_5:.2f}')
    precio_final = precio_sin_descuento - (precio_sin_descuento * 5 / 100)
    print(f'el total a pagar con descuento es: {precio_final:.2f}')
elif cantidad_pedida>=6 and cantidad_pedida <=10:
    precio_final = precio_sin_descuento - (precio_sin_descuento * 10 / 100)
    print(f'el total a pagar con descuento es: {precio_final:.2f}')
elif cantidad_pedida>10 :
    precio_final = precio_sin_descuento - (precio_sin_descuento * 15 / 100)
    print(f'el total a pagar con descuento es: {precio_final:.2f}')
else:
    print(f'no tienes descuento, tu pagas:{precio_sin_descuento:.2f}')