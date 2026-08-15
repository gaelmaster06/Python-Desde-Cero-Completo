import pandas as pd
#usando la funcion para leer el archivo CSV

#dataframe(df) es una tabla con filas y columnas
df = pd.read_csv("ARCHIVOS\\Datos.csv")
df_2 = pd.read_csv("ARCHIVOS\\Datos.csv")
#obteniendo los datos de la columna nombre
nombres =df["nombre"]
#obteniendo el dataframe por la edad
df_ordenado_ascendente  = df.sort_values("edad")

#ordenandolo por la edad de forma descendente
df_ordenado_descendente  = df.sort_values("edad",ascending=False)


#concatenando los dos dataframes
df_concatenado=pd.concat([df,df_2])

#accediendo a las primeras 2 filas con head()
primeras_filas =  df.head(2)

#accediendo a las ultimas dos filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de columnas y filas con shape
filas_totales, columas_totales = df.shape
#print(f'las filas totales son: {filas_totales} y las columnas totales son: {columas_totales}')

#obteniendo data estadistica del dataframe
df_info =df.describe()
#print(df_info)


#accediendo a la edade de la fila 2  con loc
elemento_especifico_loc =df.loc[1,"edad"]
#print(elemento_especifico_loc)

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc =df.iloc[1,2]
#print(elemento_especifico_iloc)

#accediendo a todas las filas de una columna
edad=df.iloc[:,2]
#print(edad)

#accediendo a todos los apellidos con loc
apellidos=df.loc[:,"apellido"]
print(apellidos)

#lo mismo para llamar a filas [1,:]
