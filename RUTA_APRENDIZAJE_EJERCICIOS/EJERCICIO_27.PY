#Imprime la tabla de multiplicar del 1 al 10 de un número dado por el usuario (calentamiento antes de lo pesado).
ingresa_numero=int(input("ingresa un numero para hacer su multiplicacion del 1 al 10:"))

for numero in range(1,11):
    multiplicacion= numero*ingresa_numero
    print(f'los resultados de la multiplicacion son: {multiplicacion}')

