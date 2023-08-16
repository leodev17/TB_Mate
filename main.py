from functions import *

st.header("Prueba de proyecto fhasdjhkfa")
st.subheader("Hola estimado usuario. Para continuar el analisis se requiere una matriz simetrica nxn, n>2")
num_aceptados = np.arange(30) + 3
num_aceptados = num_aceptados.astype(str)
tam = st.text_input("¿De que tamaño desea ingresar su matriz de adyacencia?")
if len(tam) > 0:
    if tam not in num_aceptados:
        st.error("Numero invalido")
    else:
        tam = int(tam)
        pedir_matriz(tam)

