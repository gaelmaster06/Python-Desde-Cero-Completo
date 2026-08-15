#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'impresionante, cometiste el siguiente error: {err}')
#lanzando mi propia excepcion
raise MiExcepcion("te equivocaste cawn")
#manejandola
try:
    raise MiExcepcion("te equivocaste otra vez")
except:
    print("dale puedes hacerlo mejor")


    
    