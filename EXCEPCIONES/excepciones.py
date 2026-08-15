#creando una funcion de sumar numeros
def sumar_dos():
#iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("ingresa un numero: ")
        b = input("ingresa otro numero: ")
        #intentando convertirlos a enterlos y sumarlos
        try:
            resultado = int(a)+int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos 
            
        except:
            print("error al sumar los numeros, asegurate de ingresar numeros")
        #si todo salio bien sal del bucle
        else:
            break
        finally:
            print("manejo de excepcion finalizado")
    #guardamos y mostramos el resultado
    return resultado

print(sumar_dos())   
