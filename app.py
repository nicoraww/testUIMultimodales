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
    
