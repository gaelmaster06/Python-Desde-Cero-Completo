#Crea una lista con 5 productos de tu cafetería (nombres) y una tupla con los 3 tamaños de vaso que manejas (chico, mediano, grande). Imprime el segundo producto y el tamaño más grande.
productos = ["latte", "frappe","capucchino","chai", "tinasa"]
tamaños =("chico", "mediano","grande")

#desempaquetando tupla
ch,md,gr = tamaños
#asi tambien se puede llamar ch seria chico, md, mediano y asi sucesivamente, la manera seria asi:  {gr}
print(f'el segundo producto es: {productos[4]} y el tamaño es: {tamaños[2]}')