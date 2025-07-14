#!/bin/bash

# Lanzar API Flask en segundo plano
echo "Iniciando API Flask..."
cd api
python3 main.py &

# Espera para que la API se levante (opcional)
sleep 2

# Lanzar la app de Streamlit
echo "Iniciando Streamlit..."
cd ../streamlit_app
streamlit run app.py --server.port=8501 --server.enableCORS=false
