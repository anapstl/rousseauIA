import streamlit as st
import requests

def mostrar_carrusel():
    ilustraciones = [
        {
            "img": "assets/Laelia_majalis.png",
            "tip": "💧 Riega por la mañana para evitar hongos.",
            "trivia": "🌼 Algunas orquídeas pueden florecer más de una vez al año."
        },
        {
            "img": "assets/Laelia_majalis.png",
            "tip": "🌤️ Coloca tus plantas cerca de ventanas con luz filtrada.",
            "trivia": "🌱 Las violetas africanas prefieren temperaturas estables."
        }
    ]

    idx = st.session_state.get("carrusel_idx", 0)
    ilustracion = ilustraciones[idx]

    st.image(ilustracion["img"], use_container_width=True)
    st.markdown(f"**Tip:** {ilustracion['tip']}")
    st.markdown(f"**Trivia:** {ilustracion['trivia']}")

    colA, colB = st.columns(2)
    if colA.button("⬅️ Anterior", key="prev"):
        st.session_state.carrusel_idx = (idx - 1) % len(ilustraciones)
    if colB.button("➡️ Siguiente", key="next"):
        st.session_state.carrusel_idx = (idx + 1) % len(ilustraciones)

def cargar_historial(api_url):
    try:
        r = requests.get(f"{api_url}/historial")
        if r.status_code == 200:
            return r.json()
    except:
        return []
    return []
