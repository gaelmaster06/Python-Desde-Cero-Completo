#Crea un validador de "orden válida para cocina": una orden solo pasa a cocina si `total_productos > 0` **y** el `metodo_pago` ya fue confirmado (`pago_confirmado = True`). Si es una orden de "cortesía" (`es_cortesia = True`), pasa sin importar el pago.
ingresa_productos = int(input('ingresa la cantidad de productos que ordenaras: '))
pago_confirmado= input('el pago fue confirmado? (si/no): ').lower() == 'si'
es_cortesia = input('¿es una orden de cortesía? (si/no): ').lower() == "si"

orden_valida = (ingresa_productos > 0 and pago_confirmado) or es_cortesia
print(f'¿La orden puede pasar a cocina? {orden_valida}') 


