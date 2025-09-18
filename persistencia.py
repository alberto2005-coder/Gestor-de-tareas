import json
import os

DATA_FILE = "tareas.json"

def inicializar_archivo():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

def cargar_tareas():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)
