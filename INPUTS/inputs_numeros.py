#pedirle un numero al usuario
#cuando quieres que un input sea un numero lo tienes que convertir para convertirlo usamos el int(variable del input) en este caso 'numero'
numero= input("Que pasa ingeniero, dame tu numero de telefono:")
#convierto el numero a entero y multiplico el numero por 2
resultado= int(numero) * 2
#convierto el numero a flotante y multiplico el numero por 2
resultado= float(numero) * 2
print(f' tu numero de telefono es: {resultado}')