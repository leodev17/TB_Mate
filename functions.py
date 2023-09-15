import pandas as pd
import streamlit as st
import numpy as np
import networkx as nx
from streamlit_option_menu import option_menu
from networkx.drawing.nx_pydot import to_pydot

nombres=[]
def pedir_matriz(tamanio):
    global nombres
    st.write("Ok, se usara una matriz ", tamanio, "x", tamanio)
    nodos = st.radio(
        "¿De qué manera desea enumerar o nombrar los nodos generados?",
        ["Numeros naturales", "Letras mayusculas", "Nombres personalizados"],
        captions=["1, 2, 3, 4, 5, ...", "A, B, C, D, E, ...", "Nodo_X1, Nodo_X2, Nodo_X3, ..."]
    )
    if nodos == "Numeros naturales":
        nombres = range(1, tamanio+1)
        nombres = [str(numero) for numero in nombres]
    elif nodos == "Letras mayusculas":
        nombres = [chr(65 + i) for i in range(tamanio)]
    elif nodos == "Nombres personalizados":
        ingreso_texto = st.text_input("Ingrese los nombres para los nodos separados por ,")
        nombres = [palabra for palabra in ingreso_texto.split(",")]
    selected = option_menu(
        menu_title=None,
        options=["Ingreso manual de terminos", "Generacion aleatoria", "Cargar CSV", "Problema de aplicacion"],
        icons=["123", "dice-5", "filetype-csv", "search"],
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Ingreso manual de terminos":
        A = np.zeros((tamanio, tamanio))
        df = pd.DataFrame(A, columns=nombres, index=nombres)
        edited_df = st.data_editor(df)
        if st.button("Confirmar matriz"):
            arr = edited_df.to_numpy()
            encontrar_componentes_conexas(edited_df)

    if selected == "Generacion aleatoria":
        arr = np.random.choice([0, 1], size=(tamanio, tamanio), p=[0.85, 0.15])
        df = pd.DataFrame(arr, index=nombres, columns=nombres)
        st.write("La matriz de adyacencia es:")
        st.dataframe(df)
        encontrar_componentes_conexas(df)

    if selected == "Cargar CSV":
        data = st.file_uploader("Cargue un archivo CSV que contenga los valores de una matriz de adyacencia simetrica, "
                              "sin encabezados y sin indices")
        if data is not None:
            data_df = pd.read_csv(data, header=None, delimiter=";")
            arr_csv = data_df.to_numpy()
            df = pd.DataFrame(arr_csv, index=nombres, columns=nombres)
            st.dataframe(df)
            encontrar_componentes_conexas(df)

    if selected == "Problema de aplicacion":
        st.write("Este concepto puede parecer muy abstracto y que no tiene mucho sentido estudiarlo. Pero "
                 "los grafos estan a nuestro alrededor y pueden usarse para describir relaciones complejas.\nA continuacion"
                 " se resolvera un pequeño problemita de grafos aplicado a un contexto real. Asi que toma un respiro "
                 "y avisame cuando te sientas preparado.")
        decision = st.radio(
            "¿Estas listo?",
            ["Mm no lo se", "***Estoy listo, vamos a por ello***", ":rainbow[Me gusta el pn]"])
        if decision == ":rainbow[Me gusta el pn]":
            st.write("Lo suponia")
        if decision == "***Estoy listo, vamos a por ello***":
            st.subheader("Problema: Red de Comunicaciones en una Empresa")
            st.write("Se tiene una empresa que acaba de incorporar a 15 nuevos empleados. Luego, se ha llevado a cabo un estudio "
                     "exhaustivo sobre las relaciones de comunicación entre los empleados durante un período específico."
                     " Se sabe que cada empleado, como fruto de un complejo intercambio de información, tiene el correo"
                     " electrónico de uno o varios compañeros, generando un conjunto de relaciones de comunicación individuales.")
            st.write("La informacion encontrada es que:")
            st.write("Ana conoce los correos de: Mia")
            st.write("Leo conoce los correos de: Eva")
            st.write("Mia conoce los correos de: Leo y Max")
            st.write("Sam conoce los correos de: Ben y Ava")
            st.write("Max conoce los correos de: Ana y Zoe")
            st.write("Eva conoce los correos de: Zoe")
            st.write("Kim conoce los correos de: Mia, Sam, Max y Zoe")
            st.write("Zoe conoce los correos de: Leo")
            st.write("Ian conoce los correos de: Leo, Mia y Ben")
            st.write("Amy conoce los correos de: Eva y Ray")
            st.write("Ben conoce los correos de: Eli")
            st.write("Eli conoce los correos de: Max e Ian")
            st.write("Ava conoce los correos de: Kim y Zoe")
            st.write("Ray conoce los correos de: Ana, Max, Kim, Ben y Pau")
            st.write("Pau conoce los correos de: Sam y Amy")
            st.write("Posteriormente, la empresa ha decidido organizar a sus empleados en varios departamentos de trabajo con "
                     "el objetivo de mejorar la eficiencia y la colaboración. Precisamente, se quiere obtener 5 departamentos compuestos por 3 empleados cada uno.")
            st.write("Se le solicita a usted como profesional que pueda modelar este problema con algun concepto "
                     "matematico y pueda sugerir una posible organizacion de los departamentos de tal forma de disminuir los problemas de comunicación."
                     "Es común que un empleado requiera mandar algún tipo de información a miembros de su mismo departamento, por lo tanto se le solicita que dé "
                     "una solución empleando el concepto de componentes conexas de un grafo.")
            st.subheader("Resolucion:")
            A = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
            nombres = ["Ana", "Leo", "Mia", "Sam", "Max", "Eva", "Kim", "Zoe", "Ian", "Amy", "Ben", "Eli", "Ava", "Ray", "Pau"]
            df = pd.DataFrame(A, columns=nombres, index=nombres)
            st.write("Primero vamos a definir una matriz de adyacencia que reflejen las relaciones del dato:")
            st.dataframe(df)
            resolver_problema(df)





def grafo_desde_df(df):
    grafo = nx.DiGraph()
    # Obtener el número de nodos en la matriz
    num_nodos = df.shape[0]

    # Agregar nodos al grafo
    grafo.add_nodes_from(nombres)  # Supongamos que los nodos están numerados desde 1

    # Recorrer la matriz de adyacencia y agregar las conexiones al grafo
    for i in nombres:
        for j in nombres:
            if df.loc[i, j] == 1:
                grafo.add_edge(i, j, weight=1)
    return grafo


def encontrar_componentes_conexas(df):
    st.text("El grafo resultante de la matriz es:")
    grafo = grafo_desde_df(df)
    dot = nx.nx_pydot.to_pydot(grafo)
    dot.set_rankdir("TB")  # Cambiar la dirección de las flechas (TB = de arriba a abajo)
    # Personalizar las aristas para que sean solo en una dirección
    for edge in dot.get_edges():
        edge.set("dir", "end")
    st.graphviz_chart(dot.to_string())
    # Convertir el DataFrame en una matriz numpy
    matriz = df.to_numpy()
    # Obtener el número de nodos en el grafo
    num_nodos = matriz.shape[0]
    # Conjunto para almacenar nodos visitados
    visitados = set()
    # Lista de conjuntos para almacenar componentes fuertemente conexas
    componentes_fuertemente_conexas = []

    # Función DFS auxiliar para encontrar el orden topologico
    def dfs_l(nodo, componente_actual):
        visitados.add(nodo)
        for vecino in df.index:
            if df.loc[nodo, vecino] == 1 and vecino not in visitados:
                dfs_l(vecino, componente_actual)
        componente_actual.insert(0, nodo)

    # Función DFS para buscar vecinos
    def dfs(nodo, componente_actual):
        visitados.add(nodo)
        componente_actual.add(nodo)
        for vecino in df.index:
            if df.loc[nodo, vecino] == 1 and vecino not in visitados:
                dfs(vecino, componente_actual)

    # Primer paso de Kosaraju: DFS para obtener el ordenamiento topológico inverso
    pila_orden = []
    for nodo in df.index:
        if nodo not in visitados:
            dfs_l(nodo, pila_orden)
    pila_orden=pila_orden[::-1]
    # Transponer la matriz para obtener el grafo dirigido inverso
    df = df.transpose()

    # Limpiar el conjunto de nodos visitados
    visitados.clear()

    # Segundo paso de Kosaraju: DFS para encontrar componentes fuertemente conexas
    while pila_orden:
        nodo = pila_orden.pop()
        if nodo not in visitados:
            componente_actual = set()
            dfs(nodo, componente_actual)
            st.write("Los nodos que conforman esta componente conexa son: " + str(componente_actual))
            SG = nx.subgraph(grafo_desde_df(df.transpose()), componente_actual)
            dot = nx.nx_pydot.to_pydot(SG)
            dot.set_rankdir("TB")  # Cambiar la dirección de las flechas (TB = de arriba a abajo)
            # Personalizar las aristas para que sean solo en una dirección
            for edge in dot.get_edges():
                edge.set("dir", "end")
            st.graphviz_chart(dot.to_string())
            componentes_fuertemente_conexas.append(componente_actual)

    for i, componente in enumerate(componentes_fuertemente_conexas):
        st.write(f"Componente {i + 1}: {componente}")


def resolver_problema(df):
    dep_A=set(nombres[:3])
    dep_B=set(nombres[3:6])
    dep_C=set(nombres[6:9])
    dep_D=set(nombres[9:12])
    dep_E=set(nombres[12:15])
    matriz = df.to_numpy()
    # Se obtiene el tamanio de la matriz cuadrada
    num_nodos = matriz.shape[0]
    # El conjunto visitados guardara los nodos que ya fueron recorridos para no volver a repetirlos
    visitados = set()
    st.text("El grafo resultante de la matriz es:")
    grafo = grafo_desde_df(df)
    # Crear un objeto dot a partir del grafo
    dot = to_pydot(grafo)
    # Cambiar el color del contorno de los nodos
    node_border_colors = {
        "Leo": "green",
        "Ana": "red",
        "Mia": "red",
        "Eva": "green",
        "Sam": "blue",
        "Max": "red",
        "Kim": "blue",
        "Zoe": "green",
        "Ian": "orange",
        "Ben": "orange",
        "Eli": "orange",
        "Amy": "purple",
        "Pau": "purple",
        "Ava": "blue",
        "Ray": "purple",
    }
    # Visualizar el grafo en Streamlit
    for node in dot.get_nodes():
        node_name = node.get_name().strip('"')  # Elimina las comillas dobles en el nombre del nodo
        node.set("color", node_border_colors.get(node_name, "black"))
    st.graphviz_chart(dot.to_string())
    # En el siguiente conjunto se guardaran otros conjuntos en el que cada uno agrupa los nodos conectados
    componentes_fuertemente_conexas = []

    # Función DFS auxiliar para encontrar el orden topologico
    def dfs_l(nodo, componente_actual):
        visitados.add(nodo)
        for vecino in df.index:
            if df.loc[nodo, vecino] == 1 and vecino not in visitados:
                dfs_l(vecino, componente_actual)
        componente_actual.insert(0, nodo)

    # Función DFS para buscar vecinos
    def dfs(nodo, componente_actual):
        visitados.add(nodo)
        componente_actual.add(nodo)
        for vecino in df.index:
            if df.loc[nodo, vecino] == 1 and vecino not in visitados:
                dfs(vecino, componente_actual)

    # Primer paso de Kosaraju: DFS para obtener el ordenamiento topológico inverso
    pila_orden = []
    for nodo in df.index:
        if nodo not in visitados:
            dfs_l(nodo, pila_orden)
    pila_orden=pila_orden[::-1]
    # Transponer la matriz para obtener el grafo dirigido inverso
    df = df.transpose()

    # Limpiar el conjunto de nodos visitados
    visitados.clear()

    # Segundo paso de Kosaraju: DFS para encontrar componentes fuertemente conexas
    while pila_orden:
        nodo = pila_orden.pop()
        if nodo not in visitados:
            componente_actual = set()
            dfs(nodo, componente_actual)
            st.write("Los nodos que conforman esta componente conexa son: " + str(componente_actual))
            SG = nx.subgraph(grafo_desde_df(df), componente_actual)
            dot = nx.nx_pydot.to_pydot(SG)
            for node in dot.get_nodes():
                node_name = node.get_name().strip('"')  # Elimina las comillas dobles en el nombre del nodo
                node.set("color", node_border_colors.get(node_name, "black"))
            dot.set_rankdir("TB")  # Cambiar la dirección de las flechas (TB = de arriba a abajo)
            # Personalizar las aristas para que sean solo en una dirección
            for edge in dot.get_edges():
                edge.set("dir", "end")
            st.graphviz_chart(dot.to_string())
            componentes_fuertemente_conexas.append(componente_actual)

    st.write("Se observa 5 componentes conexas de 3 miembros cada uno, por lo tanto se sugiere que la "
             "distribución de departamentos sea de la forma:")
    for i, componente in enumerate(componentes_fuertemente_conexas):
        st.write(f"Departamento {i + 1}: {componente}")
