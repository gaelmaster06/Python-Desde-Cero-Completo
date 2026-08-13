import csv
with open("ARCHIVOS\\Datos.csv") as archivo:
    
    reader = csv.reader(archivo)
    for row in reader:
        print(row)



    
    