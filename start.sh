#!/bin/bash
echo "🌿 Iniciando Streamlit..."
cd streamlitApp
streamlit run app.py \
  --server.port=8501 \
  --server.address=0.0.0.0 \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false &

cd ..

sleep 2

echo "🚀 Iniciando API Flask..."
python3 api/main.py 