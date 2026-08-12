#esto es para conjuntos y tuplas

animales = {"gato","perro","loro","leon"}
numeros = {10,43,23,53}

#recorriendo la conjunto animales
for animal in animales:
    print(f'ahora la variable animal es igual a:{animal}')
    
#recorriendo la conjunto numeros y multiplicando cada valor por 10 
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
#iterando dos conjuntos del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales, numeros):
    print(f'recorriendo conjunto 1: {numero}')
    print(f'recorriendo conjunto 2: {animal}')



#itera dentro de los rangos que le des en este caso de 5 a 10 iniciando desde 5 y terminando en 9
#si solo le ponemos un valor inicia en 0 y termina uno antes del que le pongas por jemplo si ponemos 5 terminara en 4 por que de 0 a 4 son 5 (0,1,2,3,4)

#for num in range(5,10):
#   print(num)

    
#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("el bucle termino")