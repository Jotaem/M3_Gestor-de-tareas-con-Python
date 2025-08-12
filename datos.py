# datos.py
# Módulo para leer y escribir tareas desde/hacia un archivo JSON.

import json
from pathlib import Path

def cargar_tareas(nombre_archivo):
    """
    Carga la lista de tareas desde un archivo JSON.
    """
    archivo = Path(nombre_archivo)
    if not archivo.exists():
        print(f"ℹ️ INFO: No se encontró '{nombre_archivo}'. Se creará uno nuevo.")
        return []

    try:
        tareas = json.loads(archivo.read_text(encoding="utf-8") or "[]")
    except json.JSONDecodeError:
        print(f"⚠️ Advertencia: El archivo '{nombre_archivo}' está corrupto. Se iniciará con una lista vacía.")
        return []
    except Exception as e:
        print(f"⚠️  Error al cargar tareas: {e}")
        return []

    return tareas

def guardar_tareas(nombre_archivo, tareas_a_guardar):
    """
    Guarda la lista de tareas en un archivo JSON.
    """
    try:
        Path(nombre_archivo).write_text(
            json.dumps(tareas_a_guardar, indent=4, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as e:
        print(f"⚠️  Error al guardar tareas: {e}")
