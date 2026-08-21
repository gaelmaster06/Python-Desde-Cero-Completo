#**(reto)** Crea un validador simple de contraseña para el acceso de empleados al POS: debe tener al menos 8 caracteres, al menos un número y al menos una mayúscula.
# - *Pista:* recorre la contraseña con un `for` y usa `.isdigit()` y `.isupper()` sobre cada carácter, guardando banderas (`True`/`False`) que actualizas si encuentras lo que buscas.

ingrese_contraseña =input('ingrese la contraseña: ')
conteo = len(ingrese_contraseña)

tiene_numero= False
tiene_mayuscula = False

for caracter  in ingrese_contraseña:
    if caracter.isdigit():
        tiene_numero=True 
    if caracter.isupper():
        tiene_mayuscula = True
if conteo >= 8 and tiene_numero and tiene_mayuscula:
    print(f'contraseña aceptada')
else:
    print(f'contraseña rechazada')       