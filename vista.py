import tkinter as tk

class VistaJuego:
    def __init__(self, root, num_pares):
        self.num_pares = num_pares
        self.botones = []  # Lista de botones que representan las cartas en la interfaz

        # Creamos un Frame donde se organizará el juego
        self.frame_juego = tk.Frame(root)
        self.frame_juego.pack()

        self.crear_tablero(self.frame_juego, num_pares)

    def crear_tablero(self, root, num_pares):
        """Crea el tablero de cartas como una cuadrícula de botones."""
        for i in range(num_pares * 2):  # 2 veces el número de pares
            boton = tk.Button(root, text="?", width=6, height=3)
            boton.grid(row=i // num_pares, column=i % num_pares)
            self.botones.append(boton)
