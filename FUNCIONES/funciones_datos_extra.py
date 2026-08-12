def frase(nombre,apellido,adjetivo):
    return f'hola{nombre}{apellido},sos muy {adjetivo}'
frase_resultante = frase('gael', 'lopez', 'bestia')
print(frase_resultante)

#utilizando keyword arguments
#frase_resultante = frase(adjetivo='bestia', nombre='gael', apellido='lopez')


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = 'tonto'):
    return f'hola{nombre}{apellido},sos muy {adjetivo}'
frase_resultante = frase('gael', 'lopez', 'inteligente')
print(frase_resultante)