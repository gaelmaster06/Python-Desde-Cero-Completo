import pandas as pd
#usando la funcion para leer el archivo CSV

#dataframe(df) es una tabla con filas y columnas
df = pd.read_csv("ARCHIVOS\\Datos.csv")

#obteniendo los datos de la columna nombre
nombres =df["nombre"]

cadena = "0123456789"

print(cadena[0:3])

