class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    pass
    #def hablar(self):
        #print("hola desde B")

class C(A):
    pass
    #def hablar(self):
        #print("hola desde C")

class D(B,C):
    pass
    #def hablar(self):
        #print("hola desde D")

d=D()
d.hablar()
#print(D.mro()) #para ver el orden de las clases en este tipo de herencias
#B.hablar(d)# para elegir desde que clase 