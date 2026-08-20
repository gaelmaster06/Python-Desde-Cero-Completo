#Pide al usuario dos números y muestra: suma, resta, multiplicación, división normal y división entera, en una sola línea cada resultado con print.
numero_1 = int(input("dame un numero crack:"))
numero_2 = int(input("dame otro numero monstruo:"))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1/ numero_2
division_entera = numero_1//numero_2
print(f'La suma de los numeros es: {suma}, la restas es: {resta}, la multiplicacion es: {multiplicacion}, la division es:{division:.2f} y la division entera es: {division_entera} ')
