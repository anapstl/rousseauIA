import streamlit as st
import requests
import os
from dotenv import load_dotenv
from utils import mostrar_carrusel, cargar_historial

load_dotenv()

st.set_page_config(
    page_title="LarousseIA 🌿",
    layout="wide"
)

API_URL = os.getenv("API_URL", "http://localhost:5000")

# background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Orchid_and_hummingbird_by_Martin_Johnson_Heade.jpg/1024px-Orchid_and_hummingbird_by_Martin_Johnson_Heade.jpg");
# Fondo con CSS
# ---------------------- STYLES ---------------------- #
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
/* Fondo general */
[data-testid="stAppViewContainer"] {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/2/2f/Martin_Johnson_Heade_-_Orchid_and_Hummingbird_near_a_Mountain_Waterfall.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
}

/* Paneles de texto */
.fondo-contenido {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(8px);
    padding: 1rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}

/* Caja de pregunta + botón */
.pregunta-container {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    display: flex;
    align-items: center;
}

input[type="text"] {
    width: 100%;
    padding: 1rem;
    border-radius: 30px;
    border: none;
    background: rgba(0,0,0,0.1);
    color: #000;
    font-size: 1rem;
    margin-right: 0.5rem;
}

button[title="Enter"] {
    background-color: #d8a59c;
    color: white;
    border: none;
    border-radius: 50%;
    width: 3rem;
    height: 3rem;
    font-size: 1.5rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

button[title="Enter"]:hover {
    background-color: #c88f86;
}

/* Scroll suave */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.2);
    border-radius: 3px;
}
</style>
""", unsafe_allow_html=True)


# Layout 20–60–20
col1, col2, col3 = st.columns([2, 6, 2], gap="large")

# ------------------------- COL 1: Carrusel -------------------------
with col1:
    st.markdown("### 🌼 Tips botánicos")
    mostrar_carrusel()

# ------------------------- COL 2: Interacción -------------------------
with col2:
    st.markdown("# LarousseIA: Jardinería de Interior 🌿")
    st.markdown("##### Tu guía visual y práctica para cuidar tus plantas")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    for entrada in reversed(st.session_state.chat):
        st.markdown(f"**Tú:** {entrada['pregunta']}")
        st.markdown(entrada['respuesta'])

    with st.container():
        st.markdown("---")
        preg = st.text_input("Haz tu pregunta:", key="input")
        if st.button("Enter"):
            # with st.spinner("Pensando..."):
            if preg.strip():
                try:
                    r = requests.get(f"{API_URL}/prompt/{preg}")
                    resp = r.json().get("respuesta", "Sin respuesta.")
                    st.session_state.chat.append({"pregunta": preg, "respuesta": resp})
                    st.rerun()
                except Exception as e:
                    st.error("No se pudo conectar con la API.")

# ------------------------- COL 3: Historial -------------------------
with col3:
    st.markdown("### 📜 Historial")
    historial = cargar_historial(API_URL)
    for item in historial:
        st.markdown(f"🕒 {item['timestamp'][:16]}")
        st.markdown(f"**🗨️ {item['pregunta']}**")
        st.markdown(f"_{item['respuesta'][:60]}..._")
        st.markdown("---")
