from grafo import *

iteraciones = 0
coloreo ={}

def coloracion_voraz(graph):

    global iteraciones 
    global coloreo
    colores = ['rojo' , 'amarillo', 'verde', 'azul']
    
    nodos = graph.grafo.keys()
    print (nodos)

    for nodo in nodos:
        colores_disponibles = set(colores)

        for vecino in graph.grafo[nodo]:
            if vecino in coloreo:
                colores_disponibles.discard(coloreo[vecino])
            
        if colores_disponibles:
            color = colores_disponibles.pop()
        else:
            color = colores[iteraciones % len(colores)]
            iteraciones = iteraciones + 1
        
        coloreo[nodo] = color

