import streamlit as st
from PIL import Image

st.title("Mi Primera App")

st.header("Portfoio NicoRaw")
st.write("IXD DESIGNER")
image = Image.open('Papi_.png)

st.image(image, caption="Pic")
