# tareas.py
# Este módulo contiene las funciones para manipular la lista de tareas (agregar, listar, marcar, eliminar).

import datos

def agregar_tarea(lista_tareas, nombre_archivo):
    """
    Permite al usuario ingresar la descripción de una nueva tarea,
    la crea como un diccionario y la añade a la lista.
    Luego, guarda la lista actualizada en el archivo.

    Args:
        lista_tareas (list): La lista actual de tareas.
        nombre_archivo (str): Nombre del archivo donde se guardarán las tareas.
    """
    descripcion = input("Ingresa la descripción de la nueva tarea: ").strip()
    if descripcion:
        tarea = {
            "descripcion": descripcion,
            "completada": False
        }
        lista_tareas.append(tarea)
        datos.guardar_tareas(nombre_archivo, lista_tareas)
        print(f"Tarea '{descripcion}' agregada con éxito.")
    else:
        print("La descripción de la tarea no puede estar vacía.")

def listar_tareas(lista_tareas):
    """
    Muestra todas las tareas presentes en la lista, indicando su número y estado.

    Args:
        lista_tareas (list): La lista actual de tareas.
    """
    if not lista_tareas:
        print("\nNo hay tareas en la lista.")
        return

    print("\n--- Tus Tareas ---")
    for i, tarea in enumerate(lista_tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i + 1}. {tarea['descripcion']} [{estado}]")
    print("------------------")

def marcar_completada(lista_tareas, nombre_archivo):
    """
    Permite al usuario seleccionar una tarea por su número para marcarla como completada.
    Guarda los cambios en el archivo.

    Args:
        lista_tareas (list): La lista actual de tareas.
        nombre_archivo (str): Nombre del archivo donde se guardarán las tareas.
    """
    if not lista_tareas:
        print("\nNo hay tareas para marcar como completadas.")
        return

    listar_tareas(lista_tareas)
    try:
        num_tarea = int(input("Ingresa el número de la tarea a marcar como completada: ").strip())
        indice_tarea = num_tarea - 1

        if 0 <= indice_tarea < len(lista_tareas):
            if not lista_tareas[indice_tarea]["completada"]:
                lista_tareas[indice_tarea]["completada"] = True
                datos.guardar_tareas(nombre_archivo, lista_tareas)
                print(f"Tarea '{lista_tareas[indice_tarea]['descripcion']}' marcada como completada.")
            else:
                print("La tarea ya estaba marcada como completada.")
        else:
            print("Número de tarea inválido. Por favor, ingresa un número que exista en la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

def eliminar_tarea(lista_tareas, nombre_archivo):
    """
    Permite al usuario seleccionar una tarea por su número para eliminarla de la lista.
    Guarda los cambios en el archivo.

    Args:
        lista_tareas (list): La lista actual de tareas.
        nombre_archivo (str): Nombre del archivo donde se guardarán las tareas.
    """
    if not lista_tareas:
        print("\nNo hay tareas para eliminar.")
        return

    listar_tareas(lista_tareas)
    try:
        num_tarea = int(input("Ingresa el número de la tarea a eliminar: ").strip())
        indice_tarea = num_tarea - 1

        if 0 <= indice_tarea < len(lista_tareas):
            tarea_eliminada = lista_tareas.pop(indice_tarea)
            datos.guardar_tareas(nombre_archivo, lista_tareas)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito.")
        else:
            print("Número de tarea inválido. Por favor, ingresa un número que exista en la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")