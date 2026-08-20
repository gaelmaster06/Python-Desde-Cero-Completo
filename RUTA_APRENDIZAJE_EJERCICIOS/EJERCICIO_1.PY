#Crea variables para tu nombre, edad, altura (float) y si eres estudiante (bool). Imprime una frase usando f-strings con las 4.
nombre = "Roberto"
edad = 21
altura = 1.71
estudiante = True
texto_estudiante = "si" if estudiante else "no"
print(f'tu nombre es: {nombre}, tu edad es: {edad}, tu estatura es: {altura} y eres estudiante? {texto_estudiante}')