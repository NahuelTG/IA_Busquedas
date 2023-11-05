# Holi 
# :D
import tkinter as tk
from collections import deque

class Estado:
    def __init__(self, mono_pos, caja1_pos, caja2_pos, platanos_pos, level=0):
        self.mono_pos = mono_pos
        self.caja1_pos = caja1_pos
        self.caja2_pos = caja2_pos
        self.platanos_pos = platanos_pos
        self.level = level

def buscar_solucion():
    estado_inicial = Estado(4, 0, 2, 7, 0)  
    cola = deque([estado_inicial])
    visitados = set([estado_inicial])

    while cola:
        estado_actual = cola.popleft()

        if estado_actual.mono_pos == estado_actual.platanos_pos:
            resultado_label.config(text=f"¡El mono ha alcanzado los plátanos en el nivel: {estado_actual.level}!")
            break
        else:
            # Mover mono
            if estado_actual.mono_pos != estado_actual.platanos_pos:
                #  mover al mono hacia los plátanos si no están en la misma posición
                if estado_actual.mono_pos < estado_actual.platanos_pos:
                    estado_actual.mono_pos += 1
                else:
                    estado_actual.mono_pos -= 1

            estado_actual.level += 1
            cola.append(estado_actual)  

# UI
raiz = tk.Tk()
raiz.title("Banana")
raiz.geometry("400x200")

inicio_boton = tk.Button(raiz, text="Iniciar Simulación", command=buscar_solucion)
inicio_boton.pack(pady=20)

# label
resultado_label = tk.Label(raiz, text="")
resultado_label.pack()


raiz.mainloop()
