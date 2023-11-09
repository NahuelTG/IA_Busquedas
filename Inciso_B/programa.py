from escenario import *
from anytree import Node, RenderTree



def crearEstadoIni():
    longitudEscenario = int(input('Ingresa el tamanio de la habitacion (en metros): '))
    mono = int(input('Ingresa en que posicion (en metros) estara el mono: '))
    x1 = int(input('Ingresa 0 para que este en el suelo o 1 para que este un nivel mas, caja1: '))
    y1 = int(input('Ingresa en que posicion (en metros) estara la primera caja: '))
    x2 = int(input('Ingresa 0 para que este en el suelo o 1 para que este un nivel mas, caja2: '))
    y2 = int(input('Ingresa en que posicion (en metros) estara la segunda caja: '))
    if(x1==0):x1=3
    else:x1=2
    if(x2==0):x2=3
    else:x2=2
    platano = int(input('Ingresa en que parte del techo (en metros) estara los platanos: '))
    matriz = crearEscenario(longitudEscenario)
    matriz = colocarObjetos(mono, [x1,y1], [x2,y2], platano, matriz)
    return matriz

def crearEstados(matriz):
    root = Node(matriz)

    if(moverDerecha != None): l1c1 = Node(moverDerecha(matriz), parent= root)
    if(moverIzquierda != None): l1c2 = Node(moverIzquierda(matriz), parent = root)
    #if(moverCajasDerecha != None): l1c3 = Node(moverCajasDerecha(matriz), parent = root)
    if(moverCajasIzquierda != None): l1c4 = Node(moverCajasIzquierda(matriz), parent = root)
    if(subirCajasDerecha != None): l1c5 = Node(subirCajasDerecha(matriz), parent = root)
    #if(subirCajasIzquierda != None): l1c6 = Node(subirCajasIzquierda(matriz), parent = root)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

def realizarAcciones(matriz):

    return 0

MATRIZ = crearEstadoIni()
print(MATRIZ)
#crearEstados(MATRIZ)
print(MATRIZ)