import streamlit as st
import requests

def mostrar_carrusel(): 
    # Lista de slides con imagen + tip + trivia
    slides = [
        {
            "tip": "Riega por la mañana para evitar hongos.",
            "trivia": "Algunas orquídeas pueden florecer más de una vez al año.",
            "img": "assets/Laelia_majalis.png",
        },
        {
            "tip": "Luz filtrada es ideal para la mayoría de las plantas de interior.",
            "trivia": "Las violetas africanas florecen todo el año si están felices.",
            "img": "assets/hortensia.jpg",
        },
        {
            "tip": "Evita cambios bruscos de temperatura cerca de tus plantas.",
            "trivia": "🪴 El ficus benjamina puede perder hojas si se estresa por el ambiente.",
            "img": "assets/iris.jpg",
        },
        {
            "tip": "Limpia las hojas con un paño húmedo para que respiren mejor.",
            "trivia": "Las plantas limpias realizan la fotosíntesis de forma más eficiente.",
            "img": "assets/rose.jpg",
        },
        {
            "tip": "Gira tus macetas cada semana para que crezcan equilibradas.",
            "trivia": "Las plantas tienden a inclinarse hacia la luz si no se giran.",
            "img": "assets/magnolia.jpg",
        },
    ]

    if "carrusel_idx" not in st.session_state:
        st.session_state.carrusel_idx = 0

    idx = st.session_state.carrusel_idx
    slide = slides[idx]

    st.markdown(f"**Tip del día:** {slide['tip']}")
    st.markdown(f"**Trivia botánica:** {slide['trivia']}")
    st.image(slide["img"], use_container_width=True)

    # col1, col2, col3 = st.columns([2, 1, 2])
    # with col1:
    #     if st.button("<", key="prev_slide"):
    #         st.session_state.carrusel_idx = (idx - 1) % len(slides)
    # with col3:
    #     if st.button(">", key="next_slide"):
    #         st.session_state.carrusel_idx = (idx + 1) % len(slides)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col2:
        if st.button("◀", key="prev_slide"):
            st.session_state.carrusel_idx = (idx - 1) % len(slides)

    with col3:
        if st.button("▶", key="next_slide"):
            st.session_state.carrusel_idx = (idx + 1) % len(slides)


def cargar_historial(api_url):
    try:
        r = requests.get(f"{api_url}/historial")
        if r.status_code == 200:
            return r.json()
    except:
        return []
    return []
