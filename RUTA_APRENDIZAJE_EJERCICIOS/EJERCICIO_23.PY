#**Proyecto mini ☕:** Calculadora de cuenta simple. Pide 3 productos y sus precios (con `input`), suma el total, y calcula el cambio si el cliente paga con un billete de $500. Si paga con menos de lo que debe, avisa "falta dinero" y di cuánto falta.

producto_1 =input("ingresa el producto 1:")
precio_1=int(input("ingresa cuanto cuesta el producto 1: "))
producto_2 =input("ingresa el producto 2:")
precio_2=int(input("ingresa cuanto cuesta el producto 2: "))
producto_3 =input("ingresa el producto 3 :")
precio_3=int(input("ingresa cuanto cuesta el producto 3: "))
total=precio_1+precio_2+precio_3
print(f"total a pagar {total}")
pago_cliente=int(input("con cuanto dinero pagaras(solo incluir numeros): "))
cambio=pago_cliente-total


if pago_cliente>total:
    print(f'tu cambio es:{cambio}')
elif pago_cliente == total:
    print(f'gracias por tu compra')
else:
    diferencia=total-pago_cliente
    print(f'faltan  {diferencia}  pesos')