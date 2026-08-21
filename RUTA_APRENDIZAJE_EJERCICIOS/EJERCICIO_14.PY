#Pide el nombre de un producto tal como lo escribiría un cajero apurado (ej. "  cafe Americano  ") y normalízalo: quita espacios (`.strip()`), y déjalo con el formato "Café Americano" (`.title()`). Esto evita que "café" y "CAFE " se traten como productos distintos en tu sistema.
ingresa_producto = input('ingresa que cafe ordenarias: ')
producto_normalizado= ingresa_producto.strip().title()
print(f'tu producto es: {producto_normalizado}')