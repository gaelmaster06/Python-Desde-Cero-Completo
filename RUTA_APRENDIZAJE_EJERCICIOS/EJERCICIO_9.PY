#Pide el total de una cuenta y clasifica el tipo de cliente según su consumo: cliente básico (menos de $50), frecuente ($50-$150), VIP (más de $150)
cuenta_total = float(input(" ingresa tu cuenta total: "))

if cuenta_total<50:
    print("el cliente se clasifica como cliente de consumo basico")
if cuenta_total>=50 and cuenta_total<=150:
    print('el cliente se clasifica como cliente de consumo frecuente')
elif cuenta_total>150:
    print('el cliente se clasifica como cliente VIP')