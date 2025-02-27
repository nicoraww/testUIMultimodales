import streamlit as st
from PIL import Image

st.title("Mi Primera App")

st.header("Portfoio NicoRaw")
st.write("IXD DESIGNER")
image = Image.open("Papi_.png")

st.image(image, caption="Pic")

texto = st.text_input("Escribe Algo")
st.write("El texto es", texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Columna 1")
  st.write("Diseño de UI Y UX")
  resp = st.checkbox("Contacto")
  if resp:
    st.write("Correcto")

with col2:
    st.subheader("Esta es la segunda columna")
    
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    
    if modo == 'Visual':
        st.write('La vista es fundamental para tu interfaz')
    
    if modo == 'auditiva':
        st.write('La audición es fundamental para tu interfaz')
    
    if modo == 'Táctil':
        st.write('El tacto es fundamental para tu interfaz')

st.subheader("Botones")

if st.button("Presiona el Botón"):
  st.write("Gracias")
else:
  st.write("No has presionado aún")

st.subheader("SelectBox")
in_mod = st.selectbox(
  "Selecciona la Modalidad",
  ("Audio", "Visual", "Háptico")
  )

if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"

st.write("La acción es:", set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )
