with open("ARCHIVOS\\bloc_de_notas.txt","w",encoding="utf-8") as archivo:
    #sobreescribiendo el archivo, si no existe lo crea, si existe lo sobrescribe
    #archivo.write('que pasa bala, impresionado?, solo estamos calentando')
    #agregando dos lineas con writelines
    archivo.writelines(['master, yo de nuevo liandotela\n', 'jajajaja\n'])
    #agregando dos lineas mas  con writelines
    archivo.writelines(['master, yo de nuevo liandotela\n', 'jajajaja\n'])