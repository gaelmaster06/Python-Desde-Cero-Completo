#30. ☕ Crea el **menú principal de tu futuro POS** en consola: se repite mostrando opciones (1. Nueva orden, 2. Ver menú, 3. Salir) hasta que el usuario escriba "salir" (usa `while True` con `break`).

while True:
    print("1.-nueva orden:(ingresa 1) ")
    print("2.-ver menu: (ingresa 2)  ")
    print("3.-salir :(ingresa 3) ")
    opcion=input("elije una opcion: ")

    if opcion=="1":
        print("procesando nueva orden...")
    elif opcion == "2":
        print("mostrando el menú...")
    elif opcion == "3":
        print("el bucle llego a su fin")
        break
    else:
        print("opción inválida, intenta de nuevo")
       

