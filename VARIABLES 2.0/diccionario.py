#creando diccionario con dict()
diccionario =dict(nombre="gael", apellido="lopez")

#las listas no pueden ser claves
#las tuplas pueden ser claves pero una lista y un conjunto no se puede, para eso se tiene que usar frozenset
#diccionario = {("nombre","apellido"): "jajaja"}



#creando diccionarios con fromkeys () valor por defecto: none
#crea claves de a,b,c,d con el valor none
#esto pasa por que el primer dato es un iterable y el segundo valor iguala el valor por defecto
diccionario= dict.fromkeys("abcd")

#creando diccionarios con fromkeys () cambiando el valor por defecto a 'crack'
diccionario=dict.fromkeys(["nombre","apellido"],'crack')


print(diccionario)
#para llamar a un solo elemento se puede llamar de la siguiente manera
print(diccionario["nombre"])

