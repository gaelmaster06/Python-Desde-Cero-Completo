#38 Usa una lambda dentro de `sorted()` para ordenar tu lista de productos del menú por precio, de más barato a más caro.  - *Pista:* `sorted(productos, key=lambda p: p["precio"])`.

productos = [
    {"nombre": "Café Americano", "precio": 35},
    {"nombre": "Muffin", "precio": 20},
    {"nombre": "Latte", "precio": 68}
]

productos_ordenados= sorted(productos, key=lambda p: p["precio"])
print(productos_ordenados)

