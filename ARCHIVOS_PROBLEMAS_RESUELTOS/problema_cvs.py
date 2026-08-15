#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("ARCHIVOS_PROBLEMAS_RESUELTOS\\Datos.csv")
#convertir a string lso datos de una columna
df['edad'] = df['edad'].astype(str)
#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#remplazando los datos de 'fermin' a 'fernando'
df['nombre'] = df['nombre'].replace('fermin','fernando', inplace = True)

#eliminando las filas con datos vacios
#df =df.dropna()   
#print(df)

#eliminando las filas duplicadas
#df=df.drop_duplicates()
#print(df)

#creando un csv con el dataframe resultando(limpio)
df.to_csv("ARCHIVOS_PROBLEMAS_RESUELTOS\Datos_limpios.csv")

