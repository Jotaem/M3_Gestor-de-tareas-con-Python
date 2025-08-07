# menu.py
# Este módulo se encarga de la interfaz de usuario del menú.

def mostrar_menu():
    """
    Imprime las opciones disponibles del menú principal en la consola.
    """
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("\n" + "-" * 50)

def obtener_opcion():
    """
    Pide al usuario que ingrese su elección y la retorna como una cadena de texto.
    """
    return input("Elige una opción: ").strip()