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
                     " Cada empleado ha mantenido comunicación con uno o varios compañeros, generando un conjunto de "
                     "relaciones de comunicación individuales.")
            st.write("Las que se encontraron son: (Ana, Amy), (Amy, Mia), (Leo, Ben), (Ben, Amy), (Max, Ava), "
                     "(Sam, Ava), (Sam, Pau), (Pau, Ava), (Eva, Ray), (Kim, Zoe), (Kim, Eli), (Eli, Ian)")
            st.write("Posteriormente, la empresa ha organizado a sus empleados en varios departamentos de trabajo con "
                     "el objetivo de mejorar la eficiencia y la colaboración.")
            st.write("Los empleados en cada departamento son:")
            st.write("Departamento A: Ana, Leo, Mia")
            st.write("Departamento B: Sam, Max, Eva")
            st.write("Departamento C: Kim, Zoe, Ian")
            st.write("Departamento D: Amy, Ben, Eli")
            st.write("Departamento E: Ava, Ray, Pau")

            st.write("Se le solicita a usted como profesional que pueda modelar este problema con algun concepto "
                     "matematico y pueda señalar en cuales de los 5 departamentos la comunicacion entre todos los"
                     " empleados del departamento podria ser posible.")
            st.subheader("Resolucion:")
            A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
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
    # En el siguiente conjunto se guardaran otros conjuntos en el que cada uno agrupa los nodos conectados
    componentes_conexas = []

    #Se recorre to.do el subgrafo con el algoritmo DFS
    def buscar_vecinos(nodo):
        # Se empieza el recorrido con el nodo seleccionado, se coloca en los nodos visitados y tambien
        # como parte de una componente conexa
        visitados.add(nodo)
        componente_actual.add(nodo)
        # Se buscaran los nodos mas cercanos con el que el nodo actual este conectado
        for vecino in df.index:
            # Si se encuentra un nuevo nodo y se encuentra conectado directamente, entonces se aplica
            # la funcion nuevamente para buscar a sus vecinos directos de este vecino.
            # Al aplicar la funcion tambien se añade este nodo al componente y se siguen buscando mas vecinos
            if df.loc[nodo, vecino] == 1 and vecino not in visitados:
                buscar_vecinos(vecino)
    st.text("El grafo resultante de la matriz es:")
    grafo = grafo_desde_df(df)
    # Crear un objeto dot a partir del grafo
    dot = to_pydot(grafo)
    # Cambiar el color del contorno de los nodos
    node_border_colors = {
        "Leo": "red",
        "Ana": "red",
        "Mia": "red",
        "Eva": "blue",
        "Sam": "blue",
        "Max": "blue",
        "Kim": "green",
        "Zoe": "green",
        "Ian": "green",
        "Ben": "orange",
        "Eli": "orange",
        "Amy": "orange",
        "Pau": "purple",
        "Ava": "purple",
        "Ray": "purple",
    }

    for node in dot.get_nodes():
        node_name = node.get_name().strip('"')  # Elimina las comillas dobles en el nombre del nodo
        node.set("color", node_border_colors.get(node_name, "black"))

    # Visualizar el grafo en Streamlit
    st.graphviz_chart(dot.to_string())
    st.write("Recordemos la distribucion de los departamentos:")
    df_dep=pd.DataFrame([list(dep_A),list(dep_B),list(dep_C),list(dep_D),list(dep_E)],
                        index=["Departamento A","Departamento B","Departamento C","Departamento D","Departamento E"],
                        columns=["Empleado 1", "Empleado 2", "Empleado 3"])
    st.dataframe(df_dep)
    st.write("Se recorrera cada componente conexa con el algoritmo DFS."
             "\nAsi que para cada nodo, se buscaran los otros nodos a los que se pueden llegar.")
    for nodo in df.index:
        if nodo not in visitados:
            st.write("Hay que elegir un nodo cualquiera, uno que no se haya recorrido antes.\n"
                     "Los nodos ya recorridos son " + str(visitados).replace("set()", "{}") + "\nPara este"
                     " caso analizaremos el nodo "+str(nodo)+" y buscaremos a todos los nodos a \nlos que pueda llegar.")
            componente_actual = set()
            buscar_vecinos(nodo)
            st.write("Los nodos que conforman esta componente conexa son: " + str(componente_actual))
            SG=nx.subgraph(grafo_desde_df(df), componente_actual)
            dot = nx.nx_pydot.to_pydot(SG)
            for node in dot.get_nodes():
                node_name = node.get_name().strip('"')  # Elimina las comillas dobles en el nombre del nodo
                node.set("color", node_border_colors.get(node_name, "black"))
            st.graphviz_chart(dot.to_string())
            componentes_conexas.append(componente_actual)
            if dep_A <= componente_actual:
                st.write("Podemos notar que en esta componente, en la que todos los nodos estan conectados, que los"
                         " miembros del Departamento A se encuentran incluidos, por lo que el Departamento A esta "
                         "totalmente comunicado.")

            if dep_B <= componente_actual:
                st.write("Podemos notar que en esta componente, en la que todos los nodos estan conectados, que los"
                         " miembros del Departamento B se encuentran incluidos, por lo que el Departamento B esta "
                         "totalmente comunicado.")

            if dep_C <= componente_actual:
                st.write("Podemos notar que en esta componente, en la que todos los nodos estan conectados, que los"
                         " miembros del Departamento C se encuentran incluidos, por lo que el Departamento C esta "
                         "totalmente comunicado.")

            if dep_D <= componente_actual:
                st.write("Podemos notar que en esta componente, en la que todos los nodos estan conectados, que los"
                         " miembros del Departamento D se encuentran incluidos, por lo que el Departamento D esta "
                         "totalmente comunicado.")

            if dep_E <= componente_actual:
                st.write("Podemos notar que en esta componente, en la que todos los nodos estan conectados, que los"
                         " miembros del Departamento E se encuentran incluidos, por lo que el Departamento E esta "
                         "totalmente comunicado.")

    st.write("Por lo tanto, la solucion de este problema es que solo los Departamentos que tienen a todos sus "
             "empleados conectados entre si son los Departamentos A y C")

    st.write("Por lo tanto, la solucion de este problema es que solo los Departamentos que tienen a todos sus "
             "empleados conectados entre si son los Departamentos A y C")
