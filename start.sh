#!/bin/bash

echo "🌿 Iniciando Streamlit..."
cd streamlitApp || exit 1

# Streamlit escucha en el puerto asignado por Render (usualmente $PORT = 10000)
streamlit run app.py \
  --server.port=$PORT \
  --server.address=0.0.0.0 \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false &

cd ..

# Flask corre solo internamente (no visible desde fuera)
python3 api/main.py
