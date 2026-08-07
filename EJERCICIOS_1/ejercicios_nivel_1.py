#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#promedio de crudos
crudo_promedio = 5
crudo_dalto = 3.5
print("--------------------------------------")
#diferencia de duracion ejercicio A
diferencia_con_min = (100-dalto_curso/otros_cursos_min*100)
print(f'el curso de dalto dura un {diferencia_con_min:.2f} % menos que el mas rapido')
diferencia_con_max = (100-dalto_curso/otros_cursos_max*100)
print((f'el curso de dalto dura un {diferencia_con_max:.2f} % menos que el mas lento'))
diferencia_con_prom = (100-dalto_curso/otros_cursos_prom*100)
print(f'el curso de dalto dura un {diferencia_con_prom:.2f} % menos que el promedio')
print("--------------------------------------")
#calculamos el porcentaje de tiempo vacio removido 
tiempo_vacio_promedio =100-otros_cursos_prom/crudo_promedio*100
tiempo_vacio_dalto =100-dalto_curso/crudo_dalto*100

#diferencia de espacios vacios que se remueven ejercicio B
print(f'el curso promedio elimina un {tiempo_vacio_promedio:.2f} % de tiempo vacio')
print(f'el curso de dalto elimina un {tiempo_vacio_dalto:.2f} % de tiempo vacio')
print("--------------------------------------")
#mostrando diferencias si los cursos duran 10 hrs
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_prom/dalto_curso*10:.2f} horas de otros cursos')
print("--------------------------------------")