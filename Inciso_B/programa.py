from escenario import *
from anytree import *
import copy



def crearEstadoIni():
    longitudEscenario = int(input('Ingresa el tamanio de la habitación (en metros): '))
    mono = int(input('Ingresa en que posición (en metros) estara el mono: '))
    x1 = int(input('Ingresa 0 para que este en el suelo o 1 para que este un nivel más arriba, Caja_1: '))
    y1 = int(input('Ingresa en que posición (en metros) estara la primera caja: '))
    x2 = int(input('Ingresa 0 para que este en el suelo o 1 para que este un nivel más arriba, Caja_2: '))
    y2 = int(input('Ingresa en que posicion (en metros) estará la segunda caja: '))
    if(x1==0):x1=3
    else:x1=2
    if(x2==0):x2=3
    else:x2=2
    platano = int(input('Ingresa en que parte del techo (en metros) estara los platanos: '))
    matriz = crearEscenario(longitudEscenario)
    matriz = colocarObjetos(mono, [x1,y1], [x2,y2], platano, matriz)
    return matriz

def crearEstados(matriz):
    
    nuevaMatriz = copy.deepcopy(matriz)
    root = Node(matriz)
    cola = [root]
    colam = [nuevaMatriz]
    recorrido = [root]
    while CogerBananas(colam[0]) == False:

        if(moverDerecha(copy.deepcopy(colam[0]))is not None): 
            l1c1 = Node(moverDerecha(copy.deepcopy(colam[0])), parent= cola[0])
            a = moverDerecha(copy.deepcopy(colam[0]))
            cola.append(l1c1)
            colam.append(a)
            recorrido.append(l1c1)
        if(moverIzquierda(copy.deepcopy(colam[0])) is not None): 
            l1c2 = Node(moverIzquierda(copy.deepcopy(colam[0])), parent = cola[0])
            b = moverIzquierda(copy.deepcopy(colam[0]))
            colam.append(b)
            cola.append(l1c2)
            recorrido.append(l1c2)
        if(moverCajasIzquierda(copy.deepcopy(colam[0])) is not None): 
            l1c4 = Node(moverCajasIzquierda(copy.deepcopy(colam[0])), parent = cola[0])
            c = moverCajasIzquierda(copy.deepcopy(colam[0]))
            colam.append(c)
            cola.append(l1c4)
            recorrido.append(l1c4)
        if(moverCajasDerecha(copy.deepcopy(colam[0])) is not None): 
            l1c3 = Node(moverCajasDerecha(copy.deepcopy(colam[0])), parent = cola[0])  
            d = moverCajasDerecha(copy.deepcopy(colam[0]))
            colam.append(d)
            cola.append(l1c3)
            recorrido.append(l1c3)
        if(subirCajasDerecha(copy.deepcopy(colam[0]))is not None): 
            l1c5 = Node(subirCajasDerecha(copy.deepcopy(colam[0])), parent = cola[0])
            e = subirCajasDerecha(copy.deepcopy(colam[0]))
            colam.append(e)
            cola.append(l1c5)
            recorrido.append(l1c5)
        if(subirCajasIzquierda(copy.deepcopy(colam[0]))is not None): 
            l1c6 = Node(subirCajasIzquierda(copy.deepcopy(colam[0])), parent = cola[0])
            f = subirCajasIzquierda(copy.deepcopy(colam[0]))
            colam.append(f)
            cola.append(l1c6)
            recorrido.append(l1c6)
        cola.pop(0)
        colam.pop(0)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    complejidad = len(list([node.name for node in PreOrderIter(root)]))
    print(f'La complejidad espacial es: {complejidad} u/e\nLa complejidad temporal es: {complejidad} u/t')
    estadoMeta = list([node.name for node in PreOrderIter(root)])
    meta = [node.name for node in PreOrderIter(root)]
    print('El estado meta es:')
    print (estadoMeta[-1])
    #w = Walker()
    #print(w.walk(root, cola[0]))

def realizarAcciones(matriz):

    return 0

matriz = crearEstadoIni()
crearEstados(copy.deepcopy(matriz))