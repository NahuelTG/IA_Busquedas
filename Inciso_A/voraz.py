from grafo import *

iteraciones = 0
cambios = 0
coloreo ={}

def coloracion_voraz(graph):

    global iteraciones 
    global cambios
    global coloreo
    colores = ['rojo' , 'amarillo', 'verde', 'azul']
    
    nodos = graph.grafo.keys()

    for nodo in nodos:
        colores_disponibles = set(colores)

        for vecino in graph.grafo[nodo]:
            if vecino in coloreo:
                colores_disponibles.discard(coloreo[vecino])
            
        if colores_disponibles:
            color = colores_disponibles.pop()
        else:
            color = colores[iteraciones % len(colores)]
            cambios +=1
        iteraciones +=1
        coloreo[nodo] = color
    costo = iteraciones + cambios
    return costo

