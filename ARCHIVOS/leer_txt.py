#leer un archivo de texto
#usando open para abrir un archivo con una codificacion universal (UTF-8)para que no falle al leer el archivo
archivo_sin_leer = open("ARCHIVOS\\bloc_de_notas.txt", encoding="utf-8")
#leer archivo completo
#archivo= archivo_sin_leer.read()

#leer archivo linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()#los parentesis son para ponerle la cantidad de caracteres que quieres que lea

#cerrar el archivo
archivo_sin_leer.close()# es importante cerrarlo para que guarde la informacion

print(linea)


