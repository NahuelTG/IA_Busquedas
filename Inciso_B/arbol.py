class Nodo:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        if hijos is None:
            hijos = []
        self.hijos = hijos

class ArbolNoBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(nuevo_nodo, self.raiz)

    def _insertar(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.hijos[0] is None:
                nodo_actual.hijos[0] = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.hijos[0])
        else:
            if nodo_actual.hijos[1] is None:
                nodo_actual.hijos[1] = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.hijos[1])

    def buscar(self, valor):
        if self.raiz is None:
            return None
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo_actual):
        if nodo_actual.valor == valor:
            return nodo_actual
        elif valor < nodo_actual.valor:
            if nodo_actual.hijos[0] is None:
                return None
            else:
                return self._buscar(valor, nodo_actual.hijos[0])
        else:
            if nodo_actual.hijos[1] is None:
                return None
            else:
                return self._buscar(valor, nodo_actual.hijos[1])

    def imprimir(self):
        if self.raiz is None:
            print("El árbol está vacío")
        else:
            self._imprimir(self.raiz)

    def _imprimir(self, nodo_actual):
        print(nodo_actual.valor)
        for hijo in nodo_actual.hijos:
            if hijo is not None:
                self._imprimir(hijo)