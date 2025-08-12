# Gestor de Tareas CLI

Este es un gestor de tareas simple basado en línea de comandos (CLI) desarrollado en Python. Permite a los usuarios organizar sus tareas diarias de manera sencilla, guardando los datos en un archivo para que la información persista entre sesiones.

## Características
- **Menú Interactivo:** Navega por las opciones a través de un menú numérico.
- **Operaciones Básicas:** Agrega, visualiza, marca como completada y elimina tareas.
- **Persistencia de Datos:** Las tareas se guardan en un archivo JSON (`tareas.json`), por lo que no se pierden al cerrar el programa.
- **Estructura Modular:** El código está organizado en diferentes módulos (`main.py`, `menu.py`, `tareas.py`, `datos.py`) para una mejor organización y mantenimiento.

## Estructura del Proyecto
- `main.py`: El punto de entrada de la aplicación. Orquesta el flujo del programa.
- `menu.py`: Contiene las funciones para mostrar el menú y capturar la entrada del usuario.
- `tareas.py`: Maneja la lógica de las operaciones con las tareas (agregar, listar, etc.).
- `datos.py`: Se encarga de la lectura y escritura de las tareas en el archivo JSON.
