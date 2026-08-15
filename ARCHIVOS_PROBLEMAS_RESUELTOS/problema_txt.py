#2 listas una con nombres otras con apellidos
nombre=["roberto","gael","frank"]
apellido=["lozano","lopez","salazar"]

#registrar esta informacion con un TXT de forma optima 
with open("nombres_Y_apellidos.txt","w") as arch:
    arch.writelines("los datos son: \n\n")
    [arch.writelines(f'Nombre: {n} \nApellido: {a}\n---------\n') for n,a in zip(nombre,apellido)]


