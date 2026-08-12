#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que le pasemos

#crear una funcion que verifique si el numero es primo
def es_prim(num):
    # verificamos que el numero pasado no pueda dividirse entre ningun numero desde 2 hasta el numero anterior al que se le paso

    for i in range(2,num):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
        #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(2,num+1):
        #verificamos si el numero es primo
      resultado = es_prim(i)
      #en caso de que sea se agrega a la lista 
      if resultado == True: primos.append(i)
      #devolvemos la lista
    return primos
#cramos el resultado llamando a la funcion y le asignamos el numero que queramos
resultado= primos_hasta(19)
#imprimimos el resultado
print(resultado)



    
