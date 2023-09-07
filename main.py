from functions import *
st.set_page_config(layout="wide")

with st.sidebar:
    st.image("UPC.png")
    selected=option_menu(
        menu_title="Menu Principal",
        options=["Presentacion del proyecto", "Enunciado del problema", "Sustento teorico", "Solucion propuesta","Creditos"],
        icons=["house", "search", "file-earmark-text-fill", "lightbulb-fill", "people"],
        menu_icon="cast",
        default_index=0
    )

if selected == "Presentacion del proyecto":
    st.title("Presentacion del proyecto")
    c1, c2 =st.columns(2)

    with c1:
        st.image("discret.jpg")
    with c2:
        st.write("El objetivo de este proyecto es demostrar las capacidades de los miembros del equipo para implementar"
                " soluciones que puedan permitir resolver problemas de contexto real con metodos computacionales.\n"
                "Para este caso, se resolvera un problema orientado a la teoria de grafos. Los grafos tienen "
                "aplicaciones fundamentales en diversas áreas del mundo real. En redes sociales, modelan conexiones "
                "entre usuarios; en navegación, optimizan rutas y mapas; en la web, representan enlaces entre sitios; "
                "en biología, describen interacciones genéticas y metabólicas; en logística, planifican transporte y "
                "distribución; en recomendaciones, impulsan sistemas de sugerencias; y en epidemiología, analizan "
                "propagación de enfermedades. También son esenciales en análisis de redes eléctricas, gestión de "
                "proyectos, interacciones proteína-proteína, y detección de fraudes financieros. Su papel en áreas "
                "como transporte, genética, redes sociales y más, los convierte en una herramienta clave para resolver "
                "problemas complejos en la actualidad.")

        st.image("graphs-real.jpg")
if selected == "Enunciado del problema":
    st.title("Enunciado del problema")
    st.header("Componentes conexas de un grafo")
    c1,c2=st.columns(2)
    with c1:
        st.write("Dados n ∈ [5, 15] ingresado por el usuario, el programa debe generar aleatoriamente una matriz booleana n×n "
                "o solicitar el ingreso de cada elemento de la matriz (según decisión del usuario). Además, debe mostrar paso "
                "a paso la transformación del grafo asociado a esta matriz hasta obtener las componentes conexas.")
        st.image("graphs-conex.jpg")

if selected == "Sustento teorico":
    st.title("Sustento teórico")
    c1, c2 = st.columns(2)
    with c1:
        st.header("¿Qué es un grafo?")
        st.write("En términos elementales podríamos definir un grafo como un conjunto de puntos (llamados elementos, "
                 "vértices, nudos o nodos) con líneas que unen pares de vértice de ellas.")
        st.image("def_g.jpg")
        st.header("¿Qué es una componente conexa?")
        st.write("La componente conexa de un grafo se refiere a un subconjunto de nodos y aristas en ese grafo donde "
                 "todos los nodos están conectados entre sí por algún camino. En otras palabras, es una porción del "
                 "grafo en la que puedes llegar desde cualquier nodo a cualquier otro nodo mediante una secuencia de "
                 "aristas. Las componentes conexas son subestructuras fundamentales en la teoría de grafos que ayudan "
                 "a dividir un grafo en regiones independientes y a comprender su conectividad. Cada componente conexa "
                 "representa una 'isla' de nodos que están interconectados dentro del grafo, y un grafo puede tener "
                 "una o varias de estas componentes. Estudiar las componentes conexas es esencial para analizar la "
                 "estructura y las propiedades de un grafo.")
        st.write("Por ejemplo, en la siguiente imagen podemos encontrar 3 componentes conexas:")
        st.image("comp.png")
    with c2:
        st.header("Algoritmo DFS y la busqueda de componentes conexas")
        st.write("El algoritmo de Búsqueda en Profundidad (Depth-First Search o DFS en inglés) es un algoritmo de "
                 "recorrido de grafos que se utiliza para explorar y analizar la estructura de un grafo.")
        st.subheader("Algoritmo DFS")
        st.write("1. Comienza en un nodo de origen dado en el grafo.\n2. Marca el nodo de origen como visitado.\n"
                 "3. Explora uno de los nodos adyacentes no visitados al nodo actual.\n4. Repite el paso 3 para el nodo "
                 "adyacente elegido y marca ese nodo como visitado.\n5. Continúa explorando los nodos adyacentes no "
                 "visitados hasta que llegues a un nodo que no tenga nodos adyacentes no visitados.\n6. Retrocede al "
                 "nodo anterior y repite el paso 3 para cualquier nodo adyacente no visitado que aún no hayas explorado.\n"
                 "Repite este proceso hasta que hayas visitado todos los nodos alcanzables desde el nodo de origen.")
        st.subheader("Encontrar Componentes Conexas con DFS:")
        st.write("Para encontrar componentes conexas en un grafo utilizando "
                 "DFS, puedes seguir estos pasos:\n1. Inicia el algoritmo DFS desde un nodo arbitrario en el grafo.\n"
                 "2. Mientras realizas el recorrido DFS, registra todos los nodos que visitas en la componente conexa actual.\n"
                 "3. Cuando el recorrido DFS llegue a un punto en el que no se puedan visitar más nodos desde el nodo "
                 "actual, habrás identificado una componente conexa completa.\n4. Continúa el proceso, seleccionando "
                 "un nodo no visitado que aún no esté en ninguna componente conexa conocida y realiza un nuevo "
                 "recorrido DFS desde ese nodo.\n5. Repite este proceso hasta que hayas encontrado todas las "
                 "componentes conexas en el grafo.")
        st.write("El algoritmo DFS es una herramienta fundamental para explorar grafos y se puede usar para "
                 "identificar componentes conexas al rastrear todos los nodos conectados a través de aristas en un "
                 "grafo. Cada componente conexa representa un conjunto de nodos que están interconectados entre sí y "
                 "se pueden encontrar mediante este proceso de búsqueda.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif")

if selected == "Solucion propuesta":
    st.title("Solucion propuesta")
    c1, c2 = st.columns([6,4])
    with c1:
        st.subheader("Hola estimado usuario. Para realizar el analisis se requiere una matriz simetrica nxn, n ∈ [5, 15]")
        num_aceptados = np.arange(11) + 5
        num_aceptados = num_aceptados.astype(str)
        tam = st.text_input("¿De que tamaño desea ingresar su matriz de adyacencia?")
        if len(tam) > 0:
            if tam not in num_aceptados:
                st.error("No sea pelotudo, literalmente ahi dice los numeros que debe ingresar")
            else:
                tam = int(tam)
                pedir_matriz(tam)

if selected == "Creditos":
    st.title("Creditos del proyecto")
    st.write("Idea del proyecto: ChatGPT")
    st.write("Algoritmos usados para el recorrido de grafos y sugerencia de las librerias utilizadas: ChatGPT")
    st.write("Experto en Streamlit que ayudo en definir funciones que den una interfaz intuitiva para el usuario: ChatGPT")
    st.write("Redaccion del contenido teorico: ChatGPT")
    st.write("Encargado de arreglar los errores del programa: ChatGPT")
    st.write("Los que haran pasar el proyecto como suyo: Demas miembros del equipo")
