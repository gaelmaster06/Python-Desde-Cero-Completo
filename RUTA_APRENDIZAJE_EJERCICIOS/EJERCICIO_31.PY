# **(reto)** ☕ Simula la **caja registradora** de tu cafetería en un turno: la caja tiene un saldo inicial (fondo de caja), y en un bucle infinito el cajero puede: registrar una venta (suma a la caja), registrar un retiro/gasto (resta de la caja), o cerrar el turno. No debe permitir retiros mayores al saldo actual de caja. Al cerrar, muestra el corte de caja final.
# # - *Pista:* estructura tu `while True` con un menú de opciones (1. Venta, 2. Retiro/gasto, 3. Cerrar turno) y usa `if/elif` dentro para cada acción, actualizando siempre la variable `saldo_caja`.
fondo_actual=1200
while True:
    print("1.-venta:(ingresa 1) ")
    print("2.-retiro/gasto: (ingresa 2)  ")
    print("3.-cerrar turno :(ingresa 3) ")
    opcion=int(input("elije una opcion: "))
    if opcion==1:
        venta=int(input("ingrese la venta realizada (en numero): "))
        fondo_actual=fondo_actual+venta
        print(f'el fondo actual es: {fondo_actual}')
        
    elif opcion==2:
        retiro=int(input("ingrese el gasto realizado (en numero): "))
        if retiro <= fondo_actual:
            fondo_actual = fondo_actual - retiro
            print(f'el fondo actual es: {fondo_actual}')
        else:
            print("no se puede realizar esta operacion, no hay suficiente saldo")
           
    elif opcion==3:
        print(f'turno cerrado')
        break
    else:
        print("invalido")
        
