import pandas as pd

# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import seaborn as sns

df = pd.read_csv("ARCHIVOS_PROBLEMAS_GRAFICOS\\pedos.csv")
#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)
#marcando el dia con mas pedos
plt.plot("01-09",15, "o")
#mostrando el grafico
plt.show()
