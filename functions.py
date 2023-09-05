import pandas as pd
import streamlit as st
import numpy as np
import networkx as nx
from streamlit_option_menu import option_menu

def pedir_matriz(tamanio):
    st.write("Ok, se usara una matriz ", tamanio, "x", tamanio)
    selected = option_menu(
        menu_title=None,
        options=["Ingreso manual de terminos", "Generacion aleatoria", "Cargar CSV"],
        icons=["123", "dice-5", "filetype-csv"],
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Ingreso manual de terminos":
        A = np.zeros((tamanio, tamanio))
        c = np.arange(tamanio)
        c = c.astype(str)
        df = pd.DataFrame(A, columns=c)
        edited_df = st.data_editor(df)
        if st.button("Confirmar matriz"):
            arr = edited_df.to_numpy()
            if (arr == arr.T).all():
                calcular_grafos(arr)
            else:
                st.error("La matriz ingresada no es simetrica")
    if selected == "Generacion aleatoria":
        arr = np.random.choice([0, 1], size=(tamanio, tamanio), p=[0.8, 0.2])
        #Nos quedamos solo con la parte superior y le sumamos la transpuesta para obtener una m. simetrica
        arr = np.triu(arr) + np.triu(arr, 1).T
        calcular_grafos(arr)
    if selected == "Cargar CSV":
        data = st.file_uploader("Cargue un archivo CSV que contenga los valores de una matriz de adyacencia simetrica, "
                              "sin encabezados y sin indices")
        if data is not None:
            data_df = pd.read_csv(data, header=None, delimiter=";")
            arr_csv = data_df.to_numpy()
            if (arr_csv != arr_csv.T).all():
                st.error("No sea pelotudo, la matriz no es simetrica, al programita le da un infarto si no es simetrica"
                         " pndejo no dura nada")
            else:
                st.dataframe(data_df)
                calcular_grafos(arr_csv)







def grafo_desde_matriz(matriz):
    grafo = nx.Graph()
    # Obtener el número de nodos en la matriz
    num_nodos = matriz.shape[0]

    # Agregar nodos al grafo
    grafo.add_nodes_from(range(1, num_nodos + 1))  # Supongamos que los nodos están numerados desde 1

    # Recorrer la matriz de adyacencia y agregar las conexiones al grafo
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if matriz[i, j] == 1:
                grafo.add_edge(i + 1, j + 1)
    return grafo


def calcular_grafos(matrix):
    grafo = grafo_desde_matriz(matrix)
    dot = nx.nx_pydot.to_pydot(grafo)
    st.graphviz_chart(dot.to_string())
    componentes_conexas = list(nx.connected_components(grafo))

    # Imprimir las componentes conexas
    for i, componente in enumerate(componentes_conexas):
        st.text("Componente " + str(i + 1) + ": " + str(componente))
