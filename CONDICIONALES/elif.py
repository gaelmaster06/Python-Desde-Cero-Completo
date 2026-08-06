ingreso_mensual = 11000
gasto_mensual = 7000
#si queremos meter dos condiciones al mismo tiempo se pueden meter condiciciones anidadas por ejemplo un if adentro de otro if
#los elif se usan para meter condiciones adicionales, es decir, si la primera condicion no se cumple entonces se ejecuta la segunda condicion y asi sucesivamente
#los elif no pueden ir despues de un else, ya que el else es la ultima condicion que se ejecuta si ninguna de las condiciones anteriores se cumple
#ejemplo de if anidados y else-if (elif)
if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Eres una persona de clase alta, pero estás en déficit.")
    elif ingreso_mensual - gasto_mensual > 4000:
        print("Eres una persona de clase alta y estas gastando moderadamente.")
    else:
        print("Eres una persona de clase alta pero estas gastando demasiado.")
elif ingreso_mensual > 5000:
    print("Eres una persona de clase media.")
elif ingreso_mensual > 2000:
    print("Eres una persona de clase media baja.")
else:
    print("Eres una persona de clase baja.")
    