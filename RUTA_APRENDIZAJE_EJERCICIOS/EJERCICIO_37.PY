#37. Convierte la función `es_par` del ejercicio 34 a una función lambda (solo para dominar la sintaxis).

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))
