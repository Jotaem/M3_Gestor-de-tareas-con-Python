# menu.py
# Este módulo se encarga de la interfaz de usuario del menú.

def mostrar_menu():
    """
    Imprime las opciones disponibles del menú principal en la consola.
    """
    print("\n" + "🔹🔸"*25)
    print("\n💻 GESTOR DE TAREAS:"+"\n")
    print("1️⃣  Agregar tarea")
    print("2️⃣  Ver tareas")
    print("3️⃣  Marcar tarea como completada")
    print("4️⃣  Eliminar tarea")
    print("5️⃣  Salir")
    print("\n" + "🔹🔸"*25 + "\n")

def obtener_opcion():

    """
    Pide al usuario que ingrese su elección y la retorna como una cadena de texto.
    """
    return input("📌 Elige una opción: ").strip()

