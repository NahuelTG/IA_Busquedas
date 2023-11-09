def crearEscenario(columnas):
    """
    Crea una matriz de dos dimensiones con valores de columnas cambiantes.
    
    Args:
        columnas: El número de columnas de la matriz.
    Returns:
        La matriz.
    """
    matriz = [[0 for i in range(columnas)] for j in range(3)]
    return matriz

def accionesMono(matriz):
    def moverMono():
        return 0
    def subirCajas():
        return 0
    def moverCajas():
        return 0
    def CogerBananas():
        return 0
    def verificarDistancias():
        return 0
    def calcularDistancias():
        return 0
    def ubicarObjetos():
        return 0


def colocarObjetos(mono, caja1, caja2, platano, matriz):
    """
    Colocara los objetos en la matriz donde:
    si es 1 sera mono.
    si es 2 sera caja.
    si es 3 sera platano.
    
    Args:
        mono: posicion del mono en la fila 3.
        caja1: posicion de la caja1 en la fila 2 o 3.
        caja2: posicion de la caja2 en la fila 2 o 3.
        platano: Posicion de los platanos en la fila 1.
        matriz: Matriz creada al inicio
    Returns:
        La matriz.
    """
    def verificarCajas(caja1, caja2):
        if(caja1[0] == 0 or caja2[0] == 0):
            return False
        if(caja1[1] == caja2[1]):
            if(caja1[0] == caja2[0]):
                return False
        if(caja1[0] == 1 and caja2[0] == 1):
            return False
        if(caja1[0] == 1 or caja2[0] == 1):
            if(caja1[1] != caja2[1]):
                return False
        if(caja1[0] == caja2[0] and caja1[1] == caja2[1]):
            return False
        if((caja1[0] == 2 or caja2[0] == 2) and (mono == caja1[1] or mono == caja2[1])):
            return False
        
        else:
            return True
    if(verificarCajas(caja1, caja2)):
        matriz[2][mono] = 1 
        matriz[caja1[0]][caja1[1]] = 2
        matriz[caja2[0]][caja2[1]] = 2
        matriz[0][platano] = 3
        return matriz
    else:
        return print("Error no se coloco los objetos")
    

matriz = crearEscenario(5)
matriz = colocarObjetos(0, [1,2], [2,2], 1, matriz)

print(matriz)