import pandas as pd

# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import seaborn as sns

df = pd.read_csv("ARCHIVOS_PROBLEMAS_GRAFICOS\\cofla_ingreso.csv")

#obteniendo el total de ingresos 
total_ingresos= df['ingresos'].sum()
print(f'el total de ingresos es: {total_ingresos}')

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#mostrando el grafico
plt.show()
