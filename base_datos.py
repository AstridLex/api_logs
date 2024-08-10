import sqlite3
from datetime import datetime

def conectar_bd():
    conn = sqlite3.connect('logs.db')
    return conn

def crear_tabla_logs():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        servicio TEXT,
                        nivel TEXT,
                        mensaje TEXT,
                        received_at TEXT
                    )''')
    conn.commit()
    conn.close()

def guardar_log(log):
    conn = conectar_bd()
    cursor = conn.cursor()
    log['received_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO logs (timestamp, servicio, nivel, mensaje, received_at)
                      VALUES (?, ?, ?, ?, ?)''', 
                   (log['timestamp'], log['servicio'], log['nivel'], log['mensaje'], log['received_at']))
    conn.commit()
    conn.close()

crear_tabla_logs()
