#Pide la hora actual (0-23) y determina si aplica el menú de "desayunos" (6-11), "comida" (12-17) o "cena/cierre" (18-23). Esto luego podría filtrar qué productos mostrar en el POS según la hora.
hora_actual = float(input("dame la hora: "))

if hora_actual >= 6 and hora_actual <=11:
    print(f'el menu es de desayunos')
elif hora_actual >=12 and hora_actual<=17:
    print(f'el menu es de comida')
elif hora_actual >=18 and hora_actual<=23:
    print(f'el menu es de cena')
else:
    print('la hora no es valida ')