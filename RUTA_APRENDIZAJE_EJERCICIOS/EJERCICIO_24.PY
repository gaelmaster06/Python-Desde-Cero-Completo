#**Proyecto mini ☕:** Registro de un producto nuevo al menú. Pide nombre, precio y categoría; valida que el precio no sea negativo ni cero (si lo es, pide de nuevo con un `while`), y guarda todo en un diccionario. Muestra el "resumen del producto registrado" al final — esto es prácticamente el formulario de "Agregar producto" que después construirás en Django.
producto_nuevo=input("ingresa el nombre del producto: ")
precio_producto=int(input("ingresa precio del producto: "))
categoria_producto=input("ingresa categoria del producto: ")



while precio_producto<=0:
    precio_producto=int(input("ingresa precio del producto: "))

guardar_producto={
    'producto': producto_nuevo,
    'precio' : precio_producto,
    'categoria': categoria_producto
}



print(guardar_producto)