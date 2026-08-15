import re
texto ="""hola crack, como estas mi titan 1.
Esta es la segunda linea de texto.
esta es la tercer linea de texto"""
resultado=re.search("segunda",texto)
#si lo encuentra devuelve true, si no devuelve none

#haciendo una busqueda simple
#resultado = re.findall("esta",texto)
#devuelve una lista con todas las palabras encontradas
#\d-> busca digitos del 0-9
#resultado = re.findall(r"\d",texto)
#\D-> busca todo menos digitos numericos del 0-9
#resultado = re.findall(r"\D",texto)

#\w -> busca letras y numeros [A-Za-z0-9_]
#resultado = re.findall(r"\w",texto)

#\W -> busca todo menos letras y numeros [^A-Za-z0-9_]
#resultado = re.findall(r"\W",texto)    
#
#\s -> busca espacios en blanco y saltos en linea
#resultado = re.findall(r"\s",texto)
#\S -> busca todo menos espacios en blanco y saltos en linea
#resultado = re.findall(r"\S",texto)
#\n -> saltos en linea
#resultado = re.findall(r"\n",texto)
#\b -> busca limites de palabras
#resultado = re.findall(r"\b",texto)
#\B -> busca limites que no son palabras
#resultado = re.findall(r"\B",texto)
#\.-> busca puntos
#resultado = re.findall(r"\.",texto)
#\\-> busca barras invertidas
#resultado = re.findall(r"\\",texto)
#\-> busca barras
#resultado = re.findall(r"/",texto)
#\t-> busca tabulaciones
#resultado = re.findall(r"\t",texto)
# -> busca cualquier caracter menos saltos en linea
#resultado = re.findall(r".",texto)
#\-> cancela caracteres especiales
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero seguido de un punto y un espacio 
#resultado=re.findall(r"\d\.\s",texto)

#\^  -> busca el comienzo de una linea
#resultado=re.findall(r"^hola",texto)

#\$ -> busca el final de una linea
#resultado=re.findall(r"texto$",texto)

#{n} busca n cantidad de veces el valor de la izquierda
#resultado=re.findall(r"a{2}",texto)


#{n,m} busca n o m veces el valor de la izquierda(al menos n, como maximo m)
#resultado=re.findall(r"a{2,3}",texto)

#| -> busca a o b
#resultado=re.findall(r"a|b",texto)

#-> busca dentro de un rango de caracteres [a-z]
#resultado=re.findall(r"[a-z]",texto)

#-> busca fuera de un rango de caracteres [^a-z]
#resultado=re.findall(r"[^a-z]",texto)

#-> busca dentro de un rango de numeros [0-9]
#resultado=re.findall(r"[0-9]",texto)

#-> busca fuera de un rango de numeros [^0-9]
#resultado=re.findall(r"[^0-9]",texto)

#-> busca dentro de un rango de caracteres especiales [!@#$]
#resultado=re.findall(r"[!@#$]",texto)

#-> busca fuera de un rango de caracteres especiales [^!@#$]
#resultado=re.findall(r"[^!@#$]",texto)

#-> busca dentro de un rango de caracteres especiales [!@#$]
#resultado=re.findall(r"[!@#$]",texto)

#-> busca fuera de un rango de caracteres especiales [^!@#$]
#resultado=re.findall(r"[^!@#$]",texto)

#-> busca dentro de un rango de caracteres especiales [!@#$]
#resultado=re.findall(r"[!@#$]",texto)

#-> busca fuera de un rango de caracteres especiales [^!@#$]
#resultado=re.findall(r"[^!@#$]",texto)

#-> busca dentro de un rango de caracteres especiales [!@#$]
#resultado=re.findall(r"[!@#$]",texto)

#-> busca fuera de un rango de caracteres especiales [^!@#$]
#resultado=re.findall(r"[^!@#$]",texto)


print(resultado)