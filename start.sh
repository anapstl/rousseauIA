#!/bin/bash

echo "🚀 Iniciando API Flask..."
python3 api/main.py &

sleep 2

echo "🌿 Iniciando Streamlit..."
cd streamlitApp
streamlit run app.py --server.port=8501 --server.enableCORS=false
