#**(reto)** ☕ Crea un diccionario que funcione como tu **menú completo** (`{"Café Americano": 35, "Capuchino": 45, "Muffin": 40}`). Usa `.get()` para buscar el precio de un producto que el cajero escriba, sin que truene el programa si el producto no existe en el menú.
#- *Pista:* `menu.get("Café Americano", "Producto no encontrado")` te devuelve un valor por defecto si la clave no existe, evitando el `KeyError`. Esto es exactamente lo que necesitarás cuando en el POS de Django alguien busque un producto que ya no existe.

menu = {
"americano caliente":50,
"americano frio":55,
"espresso":40,
"capuccino ":48,
"latte frio":68,
"latte caliente":60,
"rol":53,
"matcha caliente":65,
"matcha fria":75
}
conversion_de_producto=input("ingrese la clave de un producto: ").strip().lower()
#La linea de arriba me sirve para que aun asi la persona busque el producto con con mayusculas o minusculas siempre lo paso a minusculas pero para que esto funcione tiene que estar las claves del diccionario en minusculas no se puede tener "Americano caliente"
producto_especifico=menu.get(conversion_de_producto,"producto no encontrado")
print(producto_especifico)