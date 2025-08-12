# main.py
# archivo principal de la aplicación "Gestor de Tareas"

import datos    # Para cargar y guardar las tareas...
import tareas   # Para agregar, listar, marcar y eliminar tareas...
import menu     # Para mostrar el menú y obtener la opción del usuario...

# Nombre del archivo donde se guardarán las tareas...
NOMBRE_ARCHIVO_TAREAS = "tareas.json"

def bucle_principal():
    # Al iniciar el programa, intentamos cargar las tareas existentes desde el archivo...
    lista_tareas = datos.cargar_tareas(NOMBRE_ARCHIVO_TAREAS)

    # Bucle infinito.
    while True:
        menu.mostrar_menu()  # Muestra las opciones del menú...
        opcion = menu.obtener_opcion()  # Obtiene la opción ingresada...

        # Estructura condicional
        if opcion == '1':
            tareas.agregar_tarea(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '2':
            tareas.listar_tareas(lista_tareas)
        elif opcion == '3':
            tareas.marcar_completada(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '4':
            tareas.eliminar_tarea(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '5':
            print("✌️  Saliendo del gestor de tareas ¡Hasta pronto!")
            break
        else:
            print("⚠️  Opción no válida. Por favor, elige un número del 1️⃣  al 5️⃣  ...")

        # Pausa la ejecución y espera a que se presione Enter...
        input("\n⏎ Presiona Enter para continuar...")

if __name__ == "__main__":
    bucle_principal()  