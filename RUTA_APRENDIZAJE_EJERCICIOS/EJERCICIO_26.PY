#**(reto)** ☕ Crea un diccionario anidado que represente tu **inventario real de cafetería**: `{"Café Americano": {"precio": 35, "stock": 40}, "Muffin": {"precio": 40, "stock": 15}, ...}`. Pide un producto y una cantidad vendida, y resta del stock si hay suficiente; si no hay stock, avisa "No hay suficiente inventario". **Este ejercicio es, en esencia, tu tabla `Producto` de Django con sus campos `precio` y `stock`.**
#- *Pista:* accedes al stock con `inventario["Café Americano"]["stock"]`. Antes de restar, valida con un `if` que la cantidad pedida sea menor o igual al stock disponible.
inventario={
    "muffin":{
        "precio": 20,
        "stock" : 25,
    },
    "rol":{
        "precio": 53,
        "stock" : 20,
    },
    "chai":{
        "precio": 65,
        "stock" : 30,
    },
    "matcha":{
        "precio": 75,
        "stock" : 35,
    },
    "tisana":{
        "precio": 45,
        "stock" : 50,
    }
}
producto_vendido=input("ingrese el producto que se vendio: ").strip().lower()
cantidad_producto_vendida=int(input("ingrese la cantidad del producto que se vendio"))

if cantidad_producto_vendida<= inventario[producto_vendido]["stock"]:
    #para buscar un producto de un diccionario anidado se hace de la manera de arriba, solo me fallo eso en este ejercicio.los pasos son busca en el diccionario principal y busca en el producto que se vendia que es la variable producto_vendido si el producto coincide con uno del inventario lo buscara en stock, el la linea 30 lo hice de la manera correcta pero la linea 28 me fallo
    stock_ctualizado=inventario[producto_vendido]["stock"]-cantidad_producto_vendida
    print(f'el stock actual es: {stock_ctualizado}')
else:
    print("No hay suficiente inventario")

