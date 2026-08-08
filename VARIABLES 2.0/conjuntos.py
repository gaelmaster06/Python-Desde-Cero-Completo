#creando un conjunto con set()
conjunto = set(["dato 1", "dato 2"])


#metiendo un conjunto dentro de otro conjunto
#con frozenset se puede meter un conjunto dentro de otro conjunto pero es importante saber como  
conjunto1= frozenset(["dato 1", "dato 2"])
conjunto2= {conjunto1,"dato 3"}
print(conjunto2)

#teoria de conjuntos
conjunto1={1,3,5,7}
conjunto2={1,3,7}
#con issubset significa es un subconjunto de en este caso decimos que conjunto2 es un subconjunto de 1 
#se puede poner conjunto2<= conjunto1 y nos dara lo mismo
#la respuesta nos la da en valor booleano

#verificando si es un subconjunto
resultado= conjunto2.issubset(conjunto1)

#verificando si es un superconjunto
#con issuperset decimos que es un superconjunto, en este caso decimos que conjunto1 es un superconjunto de conjunto2
#la respuesta nos la da en valor booleano
resultado =conjunto1.issuperset(conjunto2)

#veficar si hay algun numero en comun
#cuando solo un elemento coincide de lo que estamos comparando nos dara false, si no coincide ningun elemento nos dara true
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)