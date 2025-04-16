import streamlit as st
from datetime import datetime

import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        background_css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """
        st.markdown(background_css, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .block-container {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Llama a la función con el nombre de tu imagen
set_background("Driving Range General_preview (1).jpeg")


st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# Mostrar logo centrado usando st.image() dentro de una columna
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.empty()
with col2:
    st.image("golf_seve-verde.png", width=300, caption="Bienvenido a Alhaurín Golf")
with col3:
    st.empty()


# Título
st.title("Encuesta de Satisfacción")

# Preguntas
# nombre = st.text_input("¿Cuál es tu nombre?")
experiencia = st.radio("¿Es la primera vez que juega en Alhaurín?", ["Sí", "No"])
satisfaccion = st.slider("Del 1 al 5, ¿qué tan satisfecho estás con el recorrido?", 1, 5)
servicio = st.radio("¿Cómo calificarías al personal?", ["Excelente", "Buena", "Regular", "Mala"])
Restaurante = st.radio("¿Qué le ha parecido la comida en Alhaurín Golf", ["Excelente", "Buena", "Regular", "Mala", "No he comido en el restaurante"])
comentarios = st.text_area("¿Algún comentario adicional?")

# Botón de envío
if st.button("Enviar"):
    # Guardar respuestas en un archivo
    with open("respuestas.csv", "a", encoding="utf-8") as f:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{fecha},{nombre},{satisfaccion},{servicio},{comentarios}\n")
    st.success("¡Gracias por tu opinión! 🎉")
