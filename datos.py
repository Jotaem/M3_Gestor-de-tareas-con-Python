# datos.py
# Este módulo se encarga de la lectura y escritura de datos (tareas) desde y hacia un archivo.

import json
import os

def cargar_tareas(nombre_archivo):
    """
    Carga la lista de tareas desde un archivo JSON.

    Args:
        nombre_archivo (str): La ruta y nombre del archivo JSON a cargar.

    Returns:
        list: Una lista de diccionarios que representan las tareas.
    """
    if not os.path.exists(nombre_archivo):
        print(f"INFO: No se encontró el archivo '{nombre_archivo}'. Se creará uno nuevo.")
        return []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            if not contenido:
                print(f"Advertencia: El archivo '{nombre_archivo}' está vacío. Se iniciará con una lista vacía.")
                return []
            return json.loads(contenido)
    except json.JSONDecodeError:
        print(f"Advertencia: El archivo '{nombre_archivo}' está corrupto. Se iniciará con una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar tareas: {e}")
        return []

def guardar_tareas(nombre_archivo, tareas_a_guardar):
    """
    Guarda la lista actual de tareas en un archivo JSON.

    Args:
        nombre_archivo (str): La ruta y nombre del archivo JSON donde guardar las tareas.
        tareas_a_guardar (list): La lista de diccionarios de tareas a guardar.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(tareas_a_guardar, f, indent=4)
    except Exception as e:
        print(f"Error al guardar tareas: {e}")