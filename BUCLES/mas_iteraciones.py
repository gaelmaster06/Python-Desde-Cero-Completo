frutas =["banana","manzana","pera","uva", "naranja", "kiwi", "fresa"]
cadena = "modo ingeniero"
numeros =[1,2,3,4,5]

#evitando que se coma el kiwi con la sentencia continue 
for fruta in frutas:
    if fruta == "kiwi":
        continue #salta a la siguiente iteracion
    print(f'me voy a comer una {fruta}')

#evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta =="uva":
        break#detiene el bucle
    print('bucle terminado')
else:
    print('bucle terminado sin break')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [numero*2 for numero in numeros]
print(numeros_duplicados)

#es la misma manera pero menos eficiente
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)

