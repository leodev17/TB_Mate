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
    st.title("Fue mi pn")

if selected == "Solucion propuesta":
    st.title("Solucion propuesta")
    c1, c2 = st.columns(2)
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
    st.title("Hola, xd")
