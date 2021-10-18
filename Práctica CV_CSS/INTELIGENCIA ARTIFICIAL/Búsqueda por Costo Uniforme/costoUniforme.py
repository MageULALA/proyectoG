import networkx as x   ## Libreria para grafos
from networkx.classes import graph
from networkx.classes.function import edges

G= x.Graph()
G.add_node("Z")  # creación del nodo principal
G.add_nodes_from(["a","b","c","d","e","f","h","i","g"])  #creación de hojas e hijos


graph= {                          #Hijos de nodos
    "Z":["a","b"],
    "a":["c","d"],
    "c":[],
    "d":[],
    "b":["e","f"],
    "e":["h"],
    "f":["i","g"],
    "i":[],
    "g":[]

}

def generar_bordes(graph):          # Función de Costo uniforme
    edges= []
    for node in graph:
        for vecinos in graph[node]:
            edges.append((node,vecinos))
    return edges


print("Nodos del gráfico")
print(G.nodes())
print("Ruta del Gráfico")
print(generar_bordes(graph))
