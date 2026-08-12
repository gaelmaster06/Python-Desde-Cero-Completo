
# pyrefly: ignore [missing-import]
#si el modulo estuviera dentro de una carpeta en la misma ruta

import sys
sys.path.append('c:\\Users\\gaell\\OneDrive\\Documentos\\PYTHON_DESDE_CERO\\Python-Desde-Cero-Completo\\funciones_buenas')
# pyrefly: ignore [missing-import]
import saludar as modulo_saludo

print(modulo_saludo.saludar('gael'))