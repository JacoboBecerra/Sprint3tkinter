import tkinter as tk
from tkinter import simpledialog
from modelo import JuegoMemoria
from vista import VistaJuego
from controlador import ControladorJuego


def mostrar_ventana_inicio():
    root = tk.Tk()
    root.title("Menú Principal")

    def salir():
        root.quit()

    def ver_registro():
        # Aquí puedes agregar la funcionalidad de mostrar un registro de partidas
        print("Mostrando registro de partidas...")

    def jugar():
        # Ventana para seleccionar dificultad y nombre de usuario
        dificultad = simpledialog.askstring("Seleccionar Dificultad", "Elige dificultad (fácil, media, difícil):")
        if dificultad not in ['fácil', 'media', 'difícil']:
            print("Dificultad no válida")
            return

        nombre_usuario = simpledialog.askstring("Nombre de Usuario", "Introduce tu nombre de usuario:")
        if not nombre_usuario:
            print("Nombre de usuario no válido")
            return

        # Asignamos el número de pares según la dificultad
        if dificultad == "fácil":
            num_pares = 4
        elif dificultad == "media":
            num_pares = 6
        elif dificultad == "difícil":
            num_pares = 8

        # Iniciar el juego con los parámetros elegidos
        iniciar_juego(num_pares, nombre_usuario)

    # Crear botones en la ventana principal
    boton_jugar = tk.Button(root, text="Jugar", command=jugar, width=20, height=2)
    boton_jugar.pack(pady=10)

    boton_ver_registro = tk.Button(root, text="Ver Registro de Partidas", command=ver_registro, width=20, height=2)
    boton_ver_registro.pack(pady=10)

    boton_salir = tk.Button(root, text="Salir", command=salir, width=20, height=2)
    boton_salir.pack(pady=10)

    root.mainloop()


def iniciar_juego(num_pares, nombre_usuario):
    # Ventana para iniciar el juego de memoria
    root = tk.Tk()
    root.title(f"Juego de Memoria - {nombre_usuario}")

    # Crear el modelo y la vista sin controlador
    modelo = JuegoMemoria(num_pares)
    vista = VistaJuego(root, None, num_pares)

    # Crear el controlador y conectarlo a la vista y el modelo
    controlador = ControladorJuego(vista, modelo)
    vista.configurar_controlador(controlador)  # Ahora asignamos el controlador correctamente

    # Iniciar la aplicación de tkinter
    root.mainloop()


if __name__ == "__main__":
    mostrar_ventana_inicio()