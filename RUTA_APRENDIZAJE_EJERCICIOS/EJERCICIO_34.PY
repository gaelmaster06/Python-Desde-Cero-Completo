#Crea una función `es_par(numero)` que regrese `True` o `False` (calentamiento de sintaxis).

def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False

ingresa_numero=float(input("ingresa un numero: "))
resultado=es_par(ingresa_numero)
print(f'¿Es par?: {resultado}')





