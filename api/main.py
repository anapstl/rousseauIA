from flask import Flask, request, jsonify
from llm import obtener_respuesta
from db import guardar_interaccion, obtener_historial
import logging

logging.basicConfig(
    level=logging.INFO,  # o DEBUG
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return "API de LarousseIA en línea."

@app.route("/prompt/<string:preg>")
def procesar_prompt(preg):
    logger.info(f"Pregunta recibida: {preg}")
    
    if not preg.strip():
        logger.warning("Pregunta vacía o inválida recibida.")
        return jsonify({"error": "La pregunta no puede estar vacía."}), 400

    try:
        respuesta = obtener_respuesta(preg)
        guardar_interaccion("user", preg, respuesta)
        guardar_interaccion("assistant", preg, respuesta)
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        logger.error(f"Error procesando pregunta: {e}")
        return jsonify({"error": "Ocurrió un error interno."}), 500


@app.route("/guardar", methods=["POST"])
def guardar():
    try:
        data = request.get_json()
        if not all(k in data for k in ("role", "pregunta", "respuesta")):
            logger.warning("Datos incompletos en petición /guardar.")
            return jsonify({"error": "Faltan campos requeridos (role, pregunta, respuesta)."}), 400

        if not data["pregunta"].strip() or not data["respuesta"].strip():
            logger.warning("Campos vacíos en petición /guardar.")
            return jsonify({"error": "Pregunta y respuesta no pueden estar vacíos."}), 400

        guardar_interaccion(data["role"], data["pregunta"], data["respuesta"])
        logger.info(f"Interacción guardada: {data['role']} - {data['pregunta'][:30]}...")
        return jsonify({"status": "ok"})
    except Exception as e:
        logger.error(f"Error en /guardar: {e}")
        return jsonify({"error": "Error interno al guardar."}), 500


@app.route("/historial", methods=["GET"])
def historial():
    try:
        logger.info("Solicitud de historial recibida.")
        data = obtener_historial()
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error al obtener historial: {e}")
        return jsonify({"error": "Error interno al recuperar historial."}), 500


if __name__ == "__main__":
    app.run()
