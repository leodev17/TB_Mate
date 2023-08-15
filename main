import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def grafo_desde_matriz(matriz):
    grafo = nx.Graph()
    # Obtener el número de nodos en la matriz
    num_nodos = A.shape[0]

    # Agregar nodos al grafo
    grafo.add_nodes_from(range(1, num_nodos + 1))  # Supongamos que los nodos están numerados desde 1

    # Recorrer la matriz de adyacencia y agregar las conexiones al grafo
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if A[i, j] == 1:
                grafo.add_edge(i + 1, j + 1)
    return grafo

A = np.matrix([[0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]])
grafo=grafo_desde_matriz(A)
dot = nx.nx_pydot.to_pydot(grafo)
st.graphviz_chart(dot.to_string())
componentes_conexas = list(nx.connected_components(grafo))

# Imprimir las componentes conexas
for i, componente in enumerate(componentes_conexas):
    st.text("Componente " + str(i + 1) + ": " + str(componente))
