#**(reto)** ☕ Dado un total de minutos que llevas abierta la cafetería en el día (ej. 645), calcula cuántas horas y minutos son, usando `//` y `%`. Esto lo usarás luego para saber cuánto tiempo lleva abierta la caja.
# - *Pista:* primero saca las horas totales con `minutos // 60`. Luego usa `%` para los minutos restantes.
minutos = float(input("ingresa los minutos que lleva la cafeteria abierta: "))
hora_enteras =  minutos // 60
tiempo_minutos = minutos % 60 

print(f' llevas abierto : {hora_enteras} horas y {tiempo_minutos} minutos')



