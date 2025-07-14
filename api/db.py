import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def guardar_interaccion(role, pregunta, respuesta, origen="streamlit"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO interacciones (role, pregunta, respuesta, origen)
        VALUES (%s, %s, %s, %s);
    """, (role, pregunta, respuesta, origen))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_historial(limit=5):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT * FROM interacciones
        WHERE role = 'user'
        ORDER BY timestamp DESC
        LIMIT %s;
    """, (limit,))
    preguntas = cursor.fetchall()

    # Para cada pregunta, buscar la respuesta asociada
    historial = []
    for p in preguntas:
        cursor.execute("""
            SELECT respuesta FROM interacciones
            WHERE role = 'assistant' AND pregunta = %s
            ORDER BY timestamp ASC LIMIT 1;
        """, (p['pregunta'],))
        r = cursor.fetchone()
        historial.append({
            "timestamp": p["timestamp"],
            "pregunta": p["pregunta"],
            "respuesta": r["respuesta"] if r else "[sin respuesta]"
        })

    cursor.close()
    conn.close()
    return historial

