#abriendo el archivo con with open
with open("ARCHIVOS\\bloc_de_notas.txt",encoding="utf-8" ) as archivo:

# leemos el archivo
    contenido = archivo.read()
    #mostramos el contenido
    print(contenido)

#no es necesario cerrarlo al usar with open por que se cierra automaticamente al salir del bloque
#la lectura de archivos es muy rapida en comparacion con otros procesos
