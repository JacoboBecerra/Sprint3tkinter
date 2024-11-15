import tkinter as tk
from tkinter import simpledialog, messagebox
from modelo import JuegoMemoria
from vista import VistaJuego
from controlador import ControladorJuego
from registro_partidas import RegistroPartidas


def mostrar_ventana_inicio():
    menu_root = tk.Tk()
    menu_root.title("Menú Principal")

    def salir():
        menu_root.quit()

    def ver_registro():
        """Muestra el registro de partidas en un cuadro de mensaje."""
        registro = RegistroPartidas.obtener_registro()
        mensaje = "\n".join(registro) if registro else "No hay partidas registradas aún."
        messagebox.showinfo("Registro de Partidas", mensaje)

    def jugar():
        """Selecciona dificultad y nombre del usuario antes de iniciar el juego."""
        dificultad = simpledialog.askstring("Seleccionar Dificultad", "Elige dificultad (fácil, media, difícil):")
        if dificultad not in ['fácil', 'media', 'difícil']:
            print("Dificultad no válida")
            return

        nombre_usuario = simpledialog.askstring("Nombre de Usuario", "Introduce tu nombre de usuario:")
        if not nombre_usuario:
            print("Nombre de usuario no válido")
            return

        num_pares = {"fácil": 4, "media": 6, "difícil": 8}[dificultad]
        iniciar_juego(menu_root, num_pares, nombre_usuario, dificultad)

    # Botones del menú principal
    tk.Button(menu_root, text="Jugar", command=jugar, width=20, height=2).pack(pady=10)
    tk.Button(menu_root, text="Registro de Partidas", command=ver_registro, width=20, height=2).pack(pady=10)
    tk.Button(menu_root, text="Salir", command=salir, width=20, height=2).pack(pady=10)

    menu_root.mainloop()


def iniciar_juego(menu_root, num_pares, nombre_usuario, dificultad):
    """Inicia el juego con los parámetros especificados."""
    juego_root = tk.Toplevel(menu_root)  # Creamos una ventana secundaria para el juego
    juego_root.title(f"Juego de Memoria - {nombre_usuario}")

    modelo = JuegoMemoria(num_pares)
    vista = VistaJuego(juego_root, None, num_pares)
    controlador = ControladorJuego(vista, modelo, nombre_usuario, dificultad, juego_root)
    vista.configurar_controlador(controlador)

    juego_root.mainloop()


if __name__ == "__main__":
    mostrar_ventana_inicio()

