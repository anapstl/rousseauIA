import streamlit as st
import requests

def mostrar_carrusel(): 
    # Lista de slides con imagen + tip + trivia
    slides = [
        {
            "img": "assets/Laelia_majalis.png",
            "tip": "💧 Riega por la mañana para evitar hongos.",
            "trivia": "🌼 Algunas orquídeas pueden florecer más de una vez al año."
        },
        {
            "img": "assets/Laelia_majalis.png",
            "tip": "🌤️ Luz filtrada es ideal para la mayoría de las plantas de interior.",
            "trivia": "🌿 Las violetas africanas florecen todo el año si están felices."
        },
        {
            "img": "assets/Laelia_majalis.png",
            "tip": "🌱 Evita cambios bruscos de temperatura cerca de tus plantas.",
            "trivia": "🪴 El ficus benjamina puede perder hojas si se estresa por el ambiente."
        }
    ]

    if "carrusel_idx" not in st.session_state:
        st.session_state.carrusel_idx = 0

    idx = st.session_state.carrusel_idx
    slide = slides[idx]

    st.image(slide["img"], use_container_width=True)
    st.markdown(f"**Tip del día:** {slide['tip']}")
    st.markdown(f"**Trivia botánica:** {slide['trivia']}")

    colA, colB = st.columns(2)
    with colA:
        if st.button("⬅️", key="prev_slide"):
            st.session_state.carrusel_idx = (idx - 1) % len(slides)
    with colB:
        if st.button("➡️", key="next_slide"):
            st.session_state.carrusel_idx = (idx + 1) % len(slides)

def cargar_historial(api_url):
    try:
        r = requests.get(f"{api_url}/historial")
        if r.status_code == 200:
            return r.json()
    except:
        return []
    return []
