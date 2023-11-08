class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def asignar_arista(self, nodo1, nodo2):
        if nodo1 not in self.grafo:
            self.grafo[nodo1]=[]
        if nodo2 not in self.grafo:
            self.grafo[nodo2]=[]
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)