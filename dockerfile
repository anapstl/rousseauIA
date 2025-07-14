FROM python:3.11-slim

# Crear directorio base
WORKDIR /larousseIA

# Copiar todo
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Permisos para script
RUN chmod +x start.sh

# Exponer los puertos necesarios
EXPOSE 5000 8501

# Comando de arranque
CMD ["./start.sh"]
