import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import PhotoImage
from grafo import *
from voraz import *

ventana = tk.Tk()
ventana.title("Colorear Regiones")

canvas_izquierdo = tk.Canvas(ventana, bg="#4362FA", width=400, height=500)
canvas_derecho = tk.Canvas(ventana, bg="#FFFFFF", width=400, height=500)

canvas_izquierdo.pack(side="left", fill="both", expand=True)
canvas_derecho.pack(side="right", fill="both", expand=True)

etiqueta1 = tk.Label(ventana, text="Bienvenido", font=("Ubuntu Mono", 25, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta1.place(x = 30, y=30)

etiqueta2 = tk.Label(ventana, text="Siga las instrucciones para colorear un mapa:", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta2.place(x = 30, y=90)

etiqueta3 = tk.Label(ventana, text="1. Define las regiones como nodos y las fronteras", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta3.place(x = 30, y=120)

etiqueta3 = tk.Label(ventana, text="como aristas. Como se muestra en el ejemplo. ", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta3.place(x = 30, y=140)

try:
    # Cargar la imagen
    imagen = PhotoImage(file="./mapa.png")
    imagenRedimensionada = imagen.subsample(2, 2)
    canvas_izquierdo.create_image(30, 160, anchor=tk.NW, image=imagenRedimensionada)

except tk.TclError:
    print("Hubo un problema al cargar la imagen de ejemplo.")

etiqueta4 = tk.Label(ventana, text="2. Inserte las aristas de la siguiete manera en ", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta4.place(x = 30, y=330)

etiqueta5 = tk.Label(ventana, text="en el cuadro de texto:", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta5.place(x = 30, y=350)

etiqueta6 = tk.Label(ventana, text="A B,", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta6.place(x = 100, y=370)

etiqueta7 = tk.Label(ventana, text="A C,", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta7.place(x = 100, y=385)

etiqueta8 = tk.Label(ventana, text="B C,", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta8.place(x = 100, y=400)

etiqueta9 = tk.Label(ventana, text="B D,", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta9.place(x = 100, y=415)

etiqueta10 = tk.Label(ventana, text="...", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta10.place(x = 100, y=430)

etiqueta11 = tk.Label(ventana, text="G H", font=("Ubuntu Mono", 8, "bold"), bg="#4362FA", fg="#ffffff")
etiqueta11.place(x = 100, y=445)

etiqueta12 = tk.Label(ventana, text="3. Presione Generar", font=("Ubuntu Mono", 10), bg="#4362FA", fg="#ffffff")
etiqueta12.place(x = 30, y=465)


etiqueta13 = tk.Label(ventana, text="Ingrese las aristas", font=("Ubuntu Mono", 20, "bold"), bg="#ffffff", fg="#696969")
etiqueta13.place(x = 470, y=90)


cuadro_texto = tk.Text(ventana, height=15, width=20)
cuadro_texto.place(x=510, y= 140)


grafo1 = Grafo()

def ingresar_aristas():
    entrada = cuadro_texto.get("1.0", "end-1c")
    partes = entrada.split(",")  
    for parte in partes:
        origen, destino = parte.strip().split()  
        grafo1.asignar_arista(origen, destino)
    

    print(grafo1.grafo)
    costo =coloracion_voraz(grafo1)
    print("Complejidad Temporal: ", costo, "u/t")
    print("Complejidad Espacial: ", costo, "u/e")
    print("Estado Meta:")
    print(coloreo)

    G = nx.Graph(grafo1.grafo)

    mapeo_colores = {'rojo': 'red', 'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

    for nodo, color_nombre in coloreo.items():
        color_codigo = mapeo_colores.get(color_nombre, 'gray') 
        G.add_node(nodo, color=color_codigo)

    node_colors = [G.nodes[nodo]['color'] for nodo in G.nodes]

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=10, font_color='black')

    plt.axis('off')  
    plt.title("Grafo Coloreado")
    plt.show()

def eliminar():
    cuadro_texto.delete(1.0, tk.END)
    coloreo.clear()
    grafo1.grafo.clear()
    iteraciones = 0
    cambios = 0


boton = tk.Button(ventana, text="Generar", command=ingresar_aristas, bg="#4362FA", font=("Ubuntu Mono", 15), fg="#FFFFFF" )
boton.place(x=500, y=420)

boton = tk.Button(ventana, text="Borrar", command=eliminar, bg="#4362FA", font=("Ubuntu Mono", 15), fg="#FFFFFF" )
boton.place(x=600, y=420)

ventana.mainloop()