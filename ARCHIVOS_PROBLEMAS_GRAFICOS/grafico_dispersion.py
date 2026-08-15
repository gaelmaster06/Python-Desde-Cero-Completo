import pandas as pd

# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import seaborn as sns

df = pd.read_csv("ARCHIVOS_PROBLEMAS_GRAFICOS\\dispersion.csv")

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#mostrando el grafico
plt.show()
