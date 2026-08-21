# Ruta de Ejercicios — Lógica de Programación en Python

Objetivo: reforzar cada tema del curso de SoyDalto con ejercicios de dificultad creciente, para que llegues sólido a POO. No copies soluciones de internet: intenta romperte la cabeza 15-20 min antes de ver la pista.

Regla de oro: en cada ejercicio, antes de escribir código, escribe en comentarios los **pasos en español** (pseudocódigo). Eso es lo que construye lógica, no la sintaxis.

---

## 🟦 FUNDAMENTOS

### Datos simples y Variables
1. Crea variables para tu nombre, edad, altura (float) y si eres estudiante (bool). Imprime una frase usando f-strings con las 4.
2. Pide al usuario dos números y muestra: suma, resta, multiplicación, división normal y división entera, en una sola línea cada resultado con `print`.
3. **(reto)** Intercambia el valor de dos variables `a` y `b` SIN usar una tercera variable auxiliar.
   - *Pista:* Python permite `a, b = b, a`. Intenta primero resolverlo como lo harías en otro lenguaje (con variable temporal) y luego busca la forma "pythonica".

### Datos compuestos (listas, tuplas, diccionarios - vista general)
4. ☕ Crea una lista con 5 productos de tu cafetería (nombres) y una tupla con los 3 tamaños de vaso que manejas (chico, mediano, grande). Imprime el segundo producto y el tamaño más grande.
5. ☕ Crea un diccionario que represente un producto de tu menú (nombre, precio, categoría: "bebida"/"alimento") e imprime cada valor usando las llaves. Esta va a ser la "forma base" que usarás después para TODO tu menú.

### Operadores aritméticos
6. ☕ Pide el precio de un café y la cantidad de vasos vendidos en el día; calcula el total de venta de ese producto.
7. **(reto)** ☕ Dado un total de minutos que llevas abierta la cafetería en el día (ej. 645), calcula cuántas horas y minutos son, usando `//` y `%`. Esto lo usarás luego para saber cuánto tiempo lleva abierta la caja.
   - *Pista:* primero saca las horas totales con `minutos // 60`. Luego usa `%` para los minutos restantes.

### Operadores de comparación
8. ☕ Pide el stock actual de vasos y el stock mínimo permitido; muestra si el stock actual es mayor, menor o igual al mínimo (solo con expresiones booleanas, sin `if` todavía). Esta comparación es la base de una futura "alerta de reabastecimiento" en tu POS.

### Condicionales
9. ☕ Pide el total de una cuenta y clasifica el tipo de cliente según su consumo: cliente básico (menos de $50), frecuente ($50-$150), VIP (más de $150).
10. ☕ Pide la hora actual (0-23) y determina si aplica el menú de "desayunos" (6-11), "comida" (12-17) o "cena/cierre" (18-23). Esto luego podría filtrar qué productos mostrar en el POS según la hora.
11. **(reto)** ☕ Dado el precio de un producto y la cantidad pedida en una orden, aplica un descuento tipo "combo cafetería": 5% si compra 3-5 piezas del mismo producto, 10% si compra 6-10, 15% si compra más de 10. Si compra menos de 3, sin descuento. **Este es literalmente el motor de descuentos que tu POS de Django va a necesitar.**
    - *Pista:* ordena tus `if/elif` de mayor a menor cantidad o de menor a mayor, pero sé consistente para no dejar huecos lógicos.

### Operadores lógicos
12. ☕ Crea un validador de "orden válida para cocina": una orden solo pasa a cocina si `total_productos > 0` **y** el `metodo_pago` ya fue confirmado (`pago_confirmado = True`). Si es una orden de "cortesía" (`es_cortesia = True`), pasa sin importar el pago.
13. **(reto)** ☕ Simula la validación de una promoción "2x1 en café": debe cumplirse que el cliente pida al menos 2 cafés **y** que sea antes de las 12:00, **o** que sea miércoles (día de la promo fija) sin importar la hora.
    - *Pista:* primero arma la condición de "antes de las 12 y al menos 2 cafés" combinando con `and`. Luego únela con `or` a la condición del miércoles.

---

## 🟩 SECCIÓN BÁSICA

### Métodos de cadenas
14. ☕ Pide el nombre de un producto tal como lo escribiría un cajero apurado (ej. "  cafe Americano  ") y normalízalo: quita espacios (`.strip()`), y déjalo con el formato "Café Americano" (`.title()`). Esto evita que "café" y "CAFE " se traten como productos distintos en tu sistema.
15. Pide el nombre completo de un cliente y cuenta cuántas palabras tiene usando `.split()` (útil para separar nombre y apellido al registrar clientes).
16. **(reto)** Crea un validador simple de contraseña para el acceso de empleados al POS: debe tener al menos 8 caracteres, al menos un número y al menos una mayúscula.
    - *Pista:* recorre la contraseña con un `for` y usa `.isdigit()` y `.isupper()` sobre cada carácter, guardando banderas (`True`/`False`) que actualizas si encuentras lo que buscas.

### Métodos de listas
17. ☕ Crea una lista con los productos de una orden (ej. `["Café Americano", "Muffin", "Café Americano"]`) y usa `.append()` para agregar un producto más, `.remove()` para quitar uno, `.count()` para saber cuántos cafés americanos se pidieron.
18. ☕ Simula el "carrito" de una orden: pide al usuario productos uno por uno con un `input()` en un `for` de 5 vueltas, y agrégalos a una lista con `.append()`. Al final muestra la lista completa (el "ticket" antes de cobrar).
19. **(reto)** ☕ Dada una lista con los productos vendidos en todo el día (con repetidos, ej. 30 ventas), crea una lista de "productos únicos vendidos" **sin usar `set()`**. Esto es la base para luego saber cuántos productos *distintos* tiene tu menú activo.
    - *Pista:* crea una lista vacía. Recorre la original con un `for`, y antes de agregar cada producto pregunta `if producto not in lista_nueva`.

### Métodos de diccionarios
20. ☕ Crea un diccionario de un producto de tu cafetería (nombre, precio, categoría, disponible: True/False) y usa `.keys()`, `.values()`, `.items()` para imprimir su contenido de 3 formas distintas.
21. **(reto)** ☕ Crea un diccionario que funcione como tu **menú completo** (`{"Café Americano": 35, "Capuchino": 45, "Muffin": 40}`). Usa `.get()` para buscar el precio de un producto que el cajero escriba, sin que truene el programa si el producto no existe en el menú.
    - *Pista:* `menu.get("Café Americano", "Producto no encontrado")` te devuelve un valor por defecto si la clave no existe, evitando el `KeyError`. Esto es exactamente lo que necesitarás cuando en el POS de Django alguien busque un producto que ya no existe.

### Entrada de datos (inputs)
22. ☕ Pide la cantidad de 3 productos distintos de una orden (como texto) y conviértelos a `int` para sumar el total de piezas vendidas. Maneja el caso en que el cajero escriba mal (letra en vez de número) usando `try/except`, para que el POS nunca se caiga por un error de captura.

### Ejercicios prácticos 1 (integración)
23. **Proyecto mini ☕:** Calculadora de cuenta simple. Pide 3 productos y sus precios (con `input`), suma el total, y calcula el cambio si el cliente paga con un billete de $500. Si paga con menos de lo que debe, avisa "falta dinero" y di cuánto falta.
24. **Proyecto mini ☕:** Registro de un producto nuevo al menú. Pide nombre, precio y categoría; valida que el precio no sea negativo ni cero (si lo es, pide de nuevo con un `while`), y guarda todo en un diccionario. Muestra el "resumen del producto registrado" al final — esto es prácticamente el formulario de "Agregar producto" que después construirás en Django.

---

## 🟧 SECCIÓN INTERMEDIA

### Variables 2.0 / Diccionarios 2.0
25. ☕ Crea un diccionario donde cada valor sea otra lista, representando las ventas de la semana por producto (ej. `{"Café Americano": [12, 15, 10], "Muffin": [5, 8, 6]}`). Calcula el promedio de ventas diarias de cada producto.
26. **(reto)** ☕ Crea un diccionario anidado que represente tu **inventario real de cafetería**: `{"Café Americano": {"precio": 35, "stock": 40}, "Muffin": {"precio": 40, "stock": 15}, ...}`. Pide un producto y una cantidad vendida, y resta del stock si hay suficiente; si no hay stock, avisa "No hay suficiente inventario". **Este ejercicio es, en esencia, tu tabla `Producto` de Django con sus campos `precio` y `stock`.**
    - *Pista:* accedes al stock con `inventario["Café Americano"]["stock"]`. Antes de restar, valida con un `if` que la cantidad pedida sea menor o igual al stock disponible.

### Bucle For
27. Imprime la tabla de multiplicar del 1 al 10 de un número dado por el usuario (calentamiento antes de lo pesado).
28. ☕ Dada una lista con los precios de todos los productos vendidos en un turno (ej. `[35, 40, 35, 60, 22]`), suma el total del turno usando un `for` (sin usar `sum()` todavía, para que practiques el acumulador a mano).
29. **(reto)** ☕ Dada la lista de precios del menú, calcula cuántos productos puede pedir un cliente con un presupuesto dado (ej. $150), sin pasarse del presupuesto, recorriendo el menú y acumulando.
    - *Pista:* usa una variable acumulador `total_gastado = 0` y un contador `productos_comprados = 0`. En cada vuelta pregunta si sumar el siguiente precio se pasa del presupuesto; si no, súmalo y aumenta el contador.

### Bucle While
30. ☕ Crea el **menú principal de tu futuro POS** en consola: se repite mostrando opciones (1. Nueva orden, 2. Ver menú, 3. Salir) hasta que el usuario escriba "salir" (usa `while True` con `break`).
31. **(reto)** ☕ Simula la **caja registradora** de tu cafetería en un turno: la caja tiene un saldo inicial (fondo de caja), y en un bucle infinito el cajero puede: registrar una venta (suma a la caja), registrar un retiro/gasto (resta de la caja), o cerrar el turno. No debe permitir retiros mayores al saldo actual de caja. Al cerrar, muestra el corte de caja final.
    - *Pista:* estructura tu `while True` con un menú de opciones (1. Venta, 2. Retiro/gasto, 3. Cerrar turno) y usa `if/elif` dentro para cada acción, actualizando siempre la variable `saldo_caja`.

### Funciones integradas (built-in)
32. ☕ Practica con `len()`, `sum()`, `max()`, `min()`, `sorted()`, `enumerate()` sobre una lista de ventas del día (montos de cada ticket): muestra la venta más alta, la más baja, el promedio del día y la lista ordenada de mayor a menor.
33. ☕ Usa `enumerate()` para imprimir el ticket de una orden con cada producto numerado empezando en 1 (así se ve un ticket real, no como índice de lista que empieza en 0).

### Creando funciones propias
34. Crea una función `es_par(numero)` que regrese `True` o `False` (calentamiento de sintaxis).
35. ☕ Crea una función `calcular_total_con_descuento(precio, cantidad, porcentaje_descuento)` que regrese el precio final de una línea de la orden. Esta función reemplaza directamente al ejercicio 11 pero ahora reutilizable.
36. **(reto)** ☕ Crea una función `validar_orden(carrito)` que reciba una lista de productos (diccionarios con nombre, precio, cantidad) y regrese una lista de errores encontrados (ej. `["El carrito está vacío", "Muffin tiene cantidad 0"]`). Si no hay errores, la orden está lista para cobrarse.
    - *Pista:* crea una lista vacía `errores = []` dentro de la función. Recorre el carrito con un `for` y en cada validación que falle haz `errores.append("mensaje")`. Al final, la función regresa esa lista (si está vacía, la orden es válida). Esta es exactamente la lógica de validación que usarás en las "vistas" de Django antes de guardar una orden en la base de datos.

### Funciones Lambda
37. Convierte la función `es_par` del ejercicio 34 a una función lambda (solo para dominar la sintaxis).
38. ☕ Usa una lambda dentro de `sorted()` para ordenar tu lista de productos del menú por precio, de más barato a más caro.
    - *Pista:* `sorted(productos, key=lambda p: p["precio"])`.

### Ejercicios prácticos 2 (integración)
39. **Proyecto mini ☕:** Reporte de cierre de turno. Con funciones separadas para: registrar cada venta del turno, calcular el total vendido, y clasificar el turno como "flojo" / "normal" / "excelente" según el total. Usa una lista de diccionarios para guardar cada venta (producto, precio, hora).
40. **Proyecto mini (reto grande) ☕ — Mini-POS en consola:** Este es el ejercicio más importante de toda la ruta porque es un preview directo de tu proyecto en Django. Construye:
    - Un diccionario `menu` con productos disponibles (nombre: precio).
    - Un diccionario `inventario` con el stock de cada producto (como el ejercicio 26).
    - Un `while True` como menú principal (Nueva orden / Ver ventas del día / Cerrar caja).
    - Funciones separadas: `mostrar_menu()`, `tomar_orden(menu, inventario)` (agrega productos a un carrito y descuenta del inventario), `calcular_total(carrito)`, `cobrar(carrito, efectivo_recibido)` (calcula el cambio), y `guardar_venta(carrito, historial_ventas)`.
    - Al cerrar caja, muestra el total vendido del día usando `sum()` y cuál fue el producto más vendido.
    - *Pista:* separa el problema en funciones pequeñas primero, cada una haciendo UNA sola cosa, antes de conectarlas todas en el bucle principal. No pienses en "un programa gigante": piensa en "piezas pequeñas que se hablan entre sí" — eso es exactamente cómo vas a pensar en POO (cada función de aquí se convertirá después en un método de una clase `Orden` o `Producto`), y cómo vas a pensar en Django (cada función se parecerá a una vista o a un método de modelo).

---

## 🟥 SECCIÓN SEMI AVANZADA

### Módulos y Paquetes
41. ☕ Crea un archivo `caja.py` con funciones `calcular_total`, `calcular_cambio`, `aplicar_descuento` (las que ya hiciste antes, pero ahora reutilizables). Impórtalas desde otro archivo `main.py`. Esto es literalmente separar tu "lógica de negocio" de tu "interfaz", que es como se organiza un proyecto de Django (`models.py` vs `views.py`).
42. Investiga e importa el módulo `random`: úsalo para generar un número de folio/ticket aleatorio para cada orden nueva (ej. entre 1000 y 9999).
43. **(reto)** ☕ Organiza tu lógica como un paquete real: crea una carpeta `pos_cafeteria/` con `__init__.py` y varios archivos: `productos.py` (funciones de menú/inventario), `ventas.py` (calcular total, descuento, cambio), `reportes.py` (resumen del día). Impórtalos desde `main.py`.
    - *Pista:* un paquete es simplemente una carpeta con un `__init__.py` adentro (puede estar vacío). Desde `main.py` importas así: `from pos_cafeteria.ventas import calcular_total`. Fíjate cómo esta estructura de carpetas se parece MUCHO a como Django organiza una "app" (`models.py`, `views.py`, `forms.py`).

### Archivos TXT
44. ☕ Crea un archivo `ventas_del_dia.txt` donde el programa guarde (con `with open` en modo `"a"` para no borrar lo anterior) cada venta como una línea de texto: producto, cantidad, total, hasta que el cajero escriba "cerrar caja".
45. Lee `ventas_del_dia.txt` y muestra cuántas ventas hubo en total y el contenido numerado como un mini-reporte.

### Archivos CSV
46. ☕ Crea un CSV `menu.csv` con columnas: producto, categoría, precio, stock — con al menos 8 productos reales de tu cafetería, usando el módulo `csv`. Este archivo puede ser el "seed data" que después uses para poblar tu base de datos en Django.
47. **(reto)** ☕ Crea un CSV `ventas.csv` (producto, cantidad, precio_unitario, total) simulando las ventas de un día. Léelo y calcula: el total vendido en el día, cuál fue el producto más vendido (por cantidad) y cuál generó más dinero (por total). No son lo mismo — un producto barato puede venderse mucho y otro caro poco, y necesitas distinguirlo.
    - *Pista:* usa `csv.DictReader` para leer cada fila como diccionario (`fila["total"]`). Lleva un diccionario acumulador `{"producto": total_vendido}` y ve sumando con `+=` en cada vuelta del `for`; al final usa `max()` con una `key=lambda` sobre ese diccionario para encontrar el top.

### Trabajando con archivos (general) y gráficos
48. ☕ Combina lo anterior: lee `ventas.csv` y escribe un `corte_de_caja.txt` con el resumen del día (total vendido, producto estrella, número de tickets). Este archivo es tu primer "reporte de cierre" — la versión de consola de lo que después tu POS en Django generará como PDF o vista de resumen.
49. **(reto final de esta sección) ☕:** Usa `matplotlib` para graficar (barras) las ventas por producto de tu `ventas.csv`, con los nombres de producto en el eje X y el total vendido en el eje Y. Esto es un vistazo directo a tu segundo objetivo (análisis de datos): un dueño de cafetería real necesita ver "qué se vende más" de un vistazo, no en una tabla de números.
    - *Pista:* instala con `pip install matplotlib`. La estructura mínima es: `import matplotlib.pyplot as plt`, luego `plt.bar(nombres_productos, totales_vendidos)` y `plt.show()`. Necesitas dos listas paralelas (nombres y totales) que llenas al leer el CSV.

---

## 📌 Cómo usar esta ruta

- Resuelve en orden, sin saltarte los "retos": son justo los que construyen lógica.
- Para cada ejercicio, escribe primero el pseudocódigo en comentarios, luego el código.
- Si te atoras más de 20-30 min en un reto, dime en qué ejercicio vas y te doy una pista más específica (sin darte la solución completa) o revisamos juntos tu código.
- Al terminar la Sección Semi Avanzada tendrás las bases (funciones, estructuras de datos, manejo de archivos, lógica condicional/iterativa sólida) para saltar a **POO** con una transición natural: pensarás en "convertir mis funciones y diccionarios sueltos en clases y objetos".

Cuando termines un bloque completo, dime y te propongo el siguiente set de ejercicios ya enfocados en POO (clases, atributos, métodos, herencia) conectando con tu segundo objetivo (IA/análisis de datos) y tercero (Django POS).

## 🔗 Por qué esta ruta ya te "adelanta" trabajo para tu POS en Django

No es casualidad que varios ejercicios usen menú, inventario, órdenes y caja:

- El diccionario anidado de inventario (ej. 26, 40) es literalmente la forma de tu futuro modelo `Producto` (`nombre`, `precio`, `stock`).
- La función `validar_orden()` (ej. 36) es la lógica que después vivirá en una vista de Django antes de guardar una orden.
- El mini-POS en consola (ej. 40) tiene las mismas piezas que tendrá tu app: menú, carrito, cálculo de total, cobro, guardado del historial — solo que en Django cada pieza se vuelve un modelo, una vista o un formulario en vez de una función suelta.
- Los ejercicios de CSV (46-49) son casi idénticos a cómo vas a poblar y reportar datos en una base de datos real.

Cuando lleguemos a POO, el salto natural va a ser: "estas funciones sueltas que ya hiciste, ahora las agrupamos en clases `Producto`, `Orden` y `Caja"` — y ese salto te va a costar mucho menos trabajo porque ya entendiste la lógica del negocio aquí, en Python puro.
