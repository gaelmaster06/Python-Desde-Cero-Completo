#agregar contenido a un archivo existente
with open("ARCHIVOS\\bloc_de_notas.txt","a",encoding="utf-8") as archivo:
    
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
    #agregando el archivo
        archivo.write(f'linea {i+1} agregada de forma automatica\n')
    