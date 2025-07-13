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

# Fondo con CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Orchid_and_hummingbird_by_Martin_Johnson_Heade.jpg/1024px-Orchid_and_hummingbird_by_Martin_Johnson_Heade.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.stChatMessage {{
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 1rem;
    padding: 1rem;
    margin-bottom: 1rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

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
            if preg.strip():
                try:
                    r = requests.get(f"{API_URL}/prompt/{preg}")
                    resp = r.json().get("respuesta", "Sin respuesta.")
                    st.session_state.chat.append({"pregunta": preg, "respuesta": resp})
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
