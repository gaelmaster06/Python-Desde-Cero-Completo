#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados=0
#    for numero in lista:
#        numero_sumados= numeros_sumados + numero
#    return numero_sumados

#resultado = suma([10,3,5,6,78])
#print(resultado)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado = suma_total([1,2,3,4,5,6,7,8,9])
print(resultado)


#lo mismo que arriba pero utilizando el operador * como parametro  (*args)

def suma(nombre,*numeros):
  return  f'{nombre}, la suma de tus numeros es: {sum(numeros)}'
resultado = suma('gael',4,5,6,7)
print(resultado)
