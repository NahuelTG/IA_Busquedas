def crearEscenario(columnas):
    """
    Crea una matriz de dos dimensiones con valores de columnas cambiantes.
    
    Args:
        columnas: El número de columnas de la matriz.
    Returns:
        La matriz.
    """
    matriz = [[0 for i in range(columnas)] for j in range(4)]
    return matriz


def moverIzquierda(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    
    x,y = posicion
    posNueva = (x,y - 1)
    matriz[x][y] = 0
    try:
        matriz[x][y-1] = 1
    except IndexError:
         return None
    if(posNueva == posicionCaja1 or posNueva == posicionCaja2):
        return None
    return matriz
        
def moverDerecha(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    
    x,y = posicion
    posNueva = (x,y + 1)
    matriz[x][y] = 0
    try:
        matriz[x][y+1] = 1
    except IndexError:
         return None
    if(posNueva == posicionCaja1 or posNueva == posicionCaja2):
        return None
    return matriz
        

def subirCajasDerecha(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    x,y = posicion
    if((x,y+1) == posicionCaja1 or (x,y+1) == posicionCaja2):#Subira a la derecha
        x1,y1 = posicionCaja1
        x2,y2 = posicionCaja2
        if(x1 != x2 and y1 == y2):
            matriz[x][y] = 0
            matriz[x-2][y+1] = 1 
            return matriz
        else:
            matriz[x][y] = 0
            matriz[x-1][y+1] = 1 
            return matriz
    return None
def subirCajasIzquierda(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    x,y = posicion
    if((x,y-1) == posicionCaja1 or (x,y-1) == posicionCaja2):#Subira a la Izquierda
        x1,y1 = posicionCaja1
        x2,y2 = posicionCaja2
        if(x1 != x2 and y1 == y2):
            matriz[x][y] = 0
            matriz[x-2][y-1] = 1 
            return matriz
        else:
            matriz[x][y] = 0
            matriz[x-1][y-1] = 1 
            return matriz
    return None
def moverCajasDerecha(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    x,y = posicion
    if((x,y-1) == posicionCaja1 or (x,y-1) == posicionCaja2):
        x1,y1 = posicionCaja1
        x2,y2 = posicionCaja2
        if(x1 != x2 and y1 == y2):#las cajas estan una sobre otra
            if(x1 > x2):#la caja 2 esta en la parte superior
                matriz[x2][y2] = 0
                try:matriz[x2+1][y2+2] = 3
                except IndexError: return None
                return matriz
            else:#la caja 1 esta en la parte superior
                matriz[x1][y1] = 0
                try: matriz[x1+1][y1+2] = 2
                except IndexError: return None
                return matriz
        else:#Las cajas no estan una sobre otra
            if(y-1 == y1):#movera la caja 1
                if(y+1 == y2):#la caja 2 esta al lado del mono
                    matriz[x1][y1] = 0
                    try: matriz[x1-1][y1+2] = 2
                    except IndexError: return None
                    return matriz
                else:#la caja 2 no esta al lado del mono
                    matriz[x1][y1] = 0
                    try: matriz[x1][y1+2] = 2
                    except IndexError: return None
                    return matriz
            else:#Movera la caja 2
                if(y+1 == y1):#la caja 2 esta al lado del mono
                    matriz[x2][y2] = 0
                    try: matriz[x2-1][y2+2] = 2
                    except IndexError: return None
                    return matriz
                else:#la caja 2 no esta al lado del mono
                    matriz[x2][y2] = 0
                    try: matriz[x2][y2+2] = 2
                    except IndexError: return None
                    return matriz
    return None

def moverCajasIzquierda(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionCaja1 = ubicarObjetos(matriz, 2)
    posicionCaja2 = ubicarObjetos(matriz, 3)
    x,y = posicion
    if((x,y+1) == posicionCaja1 or (x,y+1) == posicionCaja2):
        x1,y1 = posicionCaja1
        x2,y2 = posicionCaja2
        if(x1 != x2 and y1 == y2):#las cajas estan una sobre otra
            if(x1 > x2):#la caja 2 esta en la parte superior
                matriz[x2][y2] = 0
                try:matriz[x2-1][y2-2] = 3
                except IndexError: return None
                return matriz
            else:#la caja 1 esta en la parte superior
                matriz[x1][y1] = 0
                try: matriz[x1-1][y1-2] = 2
                except IndexError: return None
                return matriz
        else:#Las cajas no estan una sobre otra
            if(y+1 == y1):#movera la caja 1
                if(y-1 == y2):#la caja 2 esta al lado del mono
                    matriz[x1][y1] = 0
                    try: matriz[x1+1][y1-2] = 2
                    except IndexError: return None
                    return matriz
                else:#la caja 2 no esta al lado del mono
                    matriz[x1][y1] = 0
                    try: matriz[x1][y1-2] = 2
                    except IndexError: return None
                    return matriz
            else:#Movera la caja 2
                if(y-1 == y1):#la caja 2 esta al lado del mono
                    matriz[x2][y2] = 0
                    try: matriz[x2+1][y2-2] = 2
                    except IndexError: return None
                    return matriz
                else:#la caja 2 no esta al lado del mono
                    matriz[x2][y2] = 0
                    try: matriz[x2][y2-2] = 2
                    except IndexError: return None
                    return matriz
    return None
def CogerBananas(matriz):
    posicion = ubicarObjetos(matriz, 1)
    posicionBananas = ubicarObjetos(matriz, 4)
    x,y = posicion
    x1, y1 = posicionBananas
    if(x == 1):
        if(y == y1):
            return True
    return False
def ubicarObjetos(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return (fila, columna)
    return None



def colocarObjetos(mono, caja1, caja2, platano, matriz):
    """
    Colocara los objetos en la matriz donde:
    si es 1 sera mono.
    si es 2 sera caja1.
    si es 3 sera caja2
    si es 4 sera platano.
    
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
        if(caja1[0] == 1 or caja2[0] == 1):
             return False
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
        matriz[3][mono] = 1 
        matriz[caja1[0]][caja1[1]] = 2
        matriz[caja2[0]][caja2[1]] = 3
        matriz[0][platano] = 4
        return matriz
    else:
        return print("Error no se coloco los objetos")
    
#matriz = crearEscenario(5)
#matriz = colocarObjetos(2,[3,1],[3,3],2, matriz)
#matriz = moverCajasDerecha(matriz)
#print(matriz)