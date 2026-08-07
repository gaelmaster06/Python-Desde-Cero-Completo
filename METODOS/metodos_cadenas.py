cadena1 = "hola estoy modo-ingeniero"
cadena2 = " que locura crack, exito"
#la estructura de una cadena y de un metodo son diferentes las funciones son como dir, len, print 
#dir se pone antes de la variable y entre parentesis se pone la variable que queremos analizar, en este caso cadena1
#dir es una funcion que nos permite ver todos los metodos que podemos usar con una variable, en este caso cadena1, y nos devuelve una lista con todos los metodos que podemos usar con esa variable
resultado = dir(cadena1)
resultado = cadena1.upper() #upper es un metodo que nos permite convertir una cadena a mayusculas
resultado = cadena1.lower() #lower es un metodo que nos permite convertir una cadena a minusculas
resultado = cadena1.capitalize() #capitalize es un metodo que nos permite convertir la primera letra de una cadena a mayusculas


#metodo find e index buscan un valor

#buscamos una cadena en otra cadena, si la encuentra devuelve la posicion de la primera letra de la cadena buscada, de lo contrario devuelve -1
resultado = cadena1.find("modo") #find es un metodo que nos permite buscar una cadena en otra cadena

#index es un metodo que nos permite buscar una cadena en otra cadena, si la encuentra devuelve la posicion de la primera letra de la cadena buscada, de lo contrario devuelve un error
resultado = cadena1.index("modo")


#isnumeric es un metodo que nos permite saber si una cadena es numerica, devuelve true si la cadena es numerica, de lo contrario devuelve false
resultado = cadena1.isnumeric() 

#isalpha es un metodo que nos permite saber si una cadena es alfabetica, devuelve true si la cadena es alfabetica, de lo contrario devuelve false
resultado = cadena1.isalpha()# solamente son validos los caracteres desde la A hasta la Z, tanto mayusculas como minusculas, no se permiten espacios ni caracteres especiales

#count busca una cadena en otra caden pero este metodo que nos permite contar cuantas veces se repite una cadena en otra cadena
resultado = cadena1.count(" ")

#len es una funcion pero no un metodo, nos permite saber la longitud de una cadena, es decir, cuantas letras tiene una cadena
#contamos caracteres que tiene una funcion 

resultado = len(cadena1)

# startswith verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true, de lo contrario devuelve false
#este metodo es case sensitive, distinte entre mayusculas y minusculas
resultado= cadena1.startswith("hola")

#endwith verificamos si una cadena termina con otra cadena dada, si es asi devuelve true, de lo contrario devuelve false
#este metodo es case sensitive, distinte entre mayusculas y minusculas 
resultado = cadena1.endswith("modo-ingeniero")

#remplaza un pedazo de la cadena dada por otra dada, si no encuentra la cadena a remplazar devuelve la cadena original
resultado = cadena1.replace("modoo", "modo-dios")
#en este caso no remplaza la cadena porque modoo no se encuentra en la cadena1, por lo tanto devuelve la cadena original, si estuviera escrito modo se remplazaria por la cadena modo-dios

#separa cadenas con la cadena que le pasemos
resultado = cadena1.split(" ") #split es un metodo que nos permite separar una cadena en varias cadenas, devuelve una lista con las cadenas separadas








print(resultado)
