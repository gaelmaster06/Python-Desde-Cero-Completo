#(reto) Intercambia el valor de dos variables a y b SIN usar una tercera variable auxiliar.
#Pista: Python permite a, b = b, a. Intenta primero resolverlo como lo harías en otro lenguaje (con variable temporal) y luego busca la forma "pythonica".
a = "arbol"
b = "bigote"
a,b = b,a
print(a, b)