
#as es para cambiar el nombre del modulo y se puede usar con cualquier nombre
#se suele usar para nombres muy largos
#no es nada parecido a = asignacion
#si solo se pone import modulo_saludar no se puede cambiar el nombre

#import modulo_saludar as ms
#importando un modulo y asignando el nombre 'm_saludar'
#desde ese modulo, importamos dos funciones
# pyrefly: ignore [missing-import]
from modulo_saludar import saludar, saludar_raro

#creamos las variables con los saludos
saludo = saludar('gael')
saludo_raro = saludar_raro('frank')
#mostramos los resultados

print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(modulo_saludar))

#accedemos al nombre de este modulo
#print(__name__)#es para saber el nombre de el namespace
#module name space o espacio de nombres

#accedemos al nombre del modulo llamado
#print(modulo_saludar.__name__) 
#lo que hace es buscar el nombre de el archivo y decirte que ese es el namespace
