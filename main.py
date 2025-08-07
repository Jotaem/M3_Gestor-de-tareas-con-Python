# main.py
# Este es el archivo principal de la aplicación "Gestor de Tareas".
# Orquesta la lógica del programa, cargando datos e invocando funciones de otros módulos.

# Importamos los módulos que contienen nuestras funciones.
import datos    # Para cargar y guardar las tareas.
import tareas   # Para agregar, listar, marcar y eliminar tareas.
import menu     # Para mostrar el menú y obtener la opción del usuario.

# --- Constante de Configuración ---
# Nombre del archivo donde se guardarán las tareas.
NOMBRE_ARCHIVO_TAREAS = "tareas.json"

def bucle_principal():
    """
    Función que contiene el bucle principal de la aplicación.
    Gestiona el flujo del programa, mostrando el menú, obteniendo la opción del usuario
    y llamando a la función correspondiente.
    """
    # Al iniciar el programa, intentamos cargar las tareas existentes desde el archivo.
    lista_tareas = datos.cargar_tareas(NOMBRE_ARCHIVO_TAREAS)

    # Bucle infinito para que la aplicación se mantenga en ejecución hasta que el usuario decida salir.
    while True:
        menu.mostrar_menu()  # Muestra las opciones del menú al usuario.
        opcion = menu.obtener_opcion()  # Obtiene la opción ingresada por el usuario.

        # Estructura condicional para ejecutar la acción correspondiente.
        if opcion == '1':
            tareas.agregar_tarea(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '2':
            tareas.listar_tareas(lista_tareas)
        elif opcion == '3':
            tareas.marcar_completada(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '4':
            tareas.eliminar_tarea(lista_tareas, NOMBRE_ARCHIVO_TAREAS)
        elif opcion == '5':
            # Si el usuario elige '5', imprime un mensaje de despedida y rompe el bucle.
            print("Saliendo del gestor de tareas. ¡Hasta pronto!")
            break  # 'break' sale del bucle 'while True', finalizando el programa.
        else:
            # Si la opción ingresada no es ninguna de las válidas (1-5), muestra un mensaje de error.
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

        # Pausa la ejecución y espera a que el usuario presione Enter.
        input("\nPresiona Enter para continuar...")


# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    bucle_principal()  # Inicia la aplicación.