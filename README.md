
# 🌿 LarousseIA: Jardinería de Interior

![alt text](streamlitApp/assets/Martin_Johnson_Heade_-_Orchid_and_Hummingbird_near_a_Mountain_Waterfall.jpg)

LarousseIA es un asistente interactivo que ayuda a los amantes de las plantas a aprender y cuidar su jardín interior de forma visual, sencilla y educativa. Con una estética inspirada en la ilustración botánica clásica, ofrece respuestas en lenguaje natural, tips, y trivias que hacen que cuidar tus plantas sea más fácil y entretenido.

---

## ❓ ¿Por qué LarousseIA?

Muchas personas tienen plantas en casa, pero:

- No saben cuándo o cómo regarlas  
- Desconocen qué cuidados específicos necesita cada especie  
- Encuentran consejos confusos o demasiado técnicos  
- Olvidan lo que ya aprendieron  

---

## ✅ ¿Qué ofrece?

- Preguntas en lenguaje natural (a través de un LLM)  
- Tips y cuidados botánicos  
- Trivias y curiosidades del mundo vegetal  
- Historial de interacciones guardado en base de datos  
- Diseño visual cuidado, con fondo botánico y estilo **glassmorphism**

---

## 🧠 Arquitectura del Proyecto

- **Frontend**: Streamlit, con interfaz personalizada (CSS)  
- **Backend**: Flask API conectada a [Groq](https://groq.com)  
- **Base de datos**: PostgreSQL  
- **Despliegue**: Docker + Render.com

---

## 👤 Público objetivo

- Personas con plantas en casa o espacios interiores  
- Aficionados/as a la jardinería urbana  
- Escuelas, viveros, y tiendas ecológicas


# Organización proyecto

/larousseIA/  
├── /api/                        # Backend Flask + LLM
│   ├── main.py  
│   ├── db.py   
│   ├── llm.py  
│   └── .env.example             # Variables para Groq y PostgreSQL  
├── /streamlit_app/             # Frontend en Streamlit  
│   ├── app.py  
│   ├── /assets/                # Imágenes botánicas e ilustraciones  
│   └── utils.py                # Carrusel, helpers  
├── /sql/  
│   └── create_interacciones.sql  
├── requirements.txt  
└── README.md                         
