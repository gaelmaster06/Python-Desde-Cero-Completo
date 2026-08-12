#creando una funcion simple

def saludar():
    print('hola gael maquina ten un buen dia')
saludar()

#creando una funcion con parametros
def saludar_personas(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'guapa'
    elif sexo == 'hombre':
        adjetivo = 'bestia'
    else :
        adjetivo = 'crack'
    
    print(f'hola {nombre}, mi {adjetivo} ten un buen dia')
saludar_personas('gael','HOMBRE')
saludar_personas('ashly','MUJER')

#CREAR UNA FUNCION QUE NOS RETORNE VALORES
# Definimos la función que recibe un número como parámetro
def crear_contraseña_random(num):
    chars = 'abcdefghij'     # Cadena con 10 caracteres (índices 0 al 9)
    num_entero = str(num)   #Convierte el número recibido a texto (string)
    num =int(num_entero[0]) # Toma solo el primer dígito del número y lo vuelve a convertir a entero
      # Calculamos 3 índices para acceder a la cadena 'chars'
    c1= num -2
    c2= num
    c3= num+2
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}'
     # Retornamos la contraseña generada
    return contraseña
# Guardamos el resultado devuelto por la función en una variable
password = crear_contraseña_random(5)
print(password)               