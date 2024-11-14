import tkinter as tk


class VistaJuego:
    def __init__(self, root, controlador, num_pares):
        self.controlador = controlador
        self.num_pares = num_pares  # Guardamos num_pares como atributo de la instancia
        self.botones = []

        # Creamos un Frame donde se organizará el juego
        self.frame_juego = tk.Frame(root)
        self.frame_juego.pack()

        self.crear_tablero(self.frame_juego, num_pares)
        self.boton_reiniciar = None  # Guardar referencia para después
        self.crear_boton_reiniciar(self.frame_juego)

        self.mensaje_ganador = None  # Para almacenar el mensaje de ganador

    def crear_tablero(self, root, num_pares):
        """Crea el tablero de cartas como una cuadrícula de botones."""
        for i in range(num_pares * 2):
            boton = tk.Button(root, text="?", width=6, height=3, command=lambda i=i: self.controlador.voltear_carta(i))
            boton.grid(row=i // num_pares, column=i % num_pares)
            self.botones.append(boton)

    def crear_boton_reiniciar(self, root):
        """Crea el botón de reinicio en la interfaz, sin el comando inicialmente."""
        self.boton_reiniciar = tk.Button(root, text="Reiniciar")
        self.boton_reiniciar.grid(row=self.num_pares, column=0, columnspan=self.num_pares, sticky="ew", pady=10)

    def configurar_controlador(self, controlador):
        """Configura el controlador y añade el comando al botón de reinicio."""
        self.controlador = controlador
        self.boton_reiniciar.config(command=self.controlador.reiniciar_juego)

    def mostrar_valor_carta(self, indice, valor):
        """Muestra el valor de la carta en el botón."""
        self.botones[indice].config(text=str(valor), state="disabled")

    def ocultar_valor_carta(self, indice):
        """Oculta el valor de la carta en el botón."""
        self.botones[indice].config(text="?", state="normal")

    def desactivar_carta(self, indice):
        """Desactiva el botón de la carta encontrada."""
        self.botones[indice].config(state="disabled")

    def mostrar_mensaje_ganador(self):
        """Muestra un mensaje cuando el jugador gana dentro de la ventana del juego."""
        if self.mensaje_ganador:  # Si ya existe el mensaje, lo eliminamos antes de mostrar uno nuevo
            self.mensaje_ganador.destroy()

        # Crear el mensaje de ganador y colocarlo debajo de las cartas
        self.mensaje_ganador = tk.Label(self.frame_juego, text="¡Has ganado!", font=('Helvetica', 16))
        self.mensaje_ganador.grid(row=self.num_pares + 1, column=0, columnspan=self.num_pares, pady=20)

    def reiniciar_tablero(self):
        """Reinicia el tablero ocultando todas las cartas y eliminando el mensaje de ganador."""
        # Ocultar todas las cartas
        for boton in self.botones:
            boton.config(text="?", state="normal")

        # Si el mensaje de ganador está presente, lo destruimos
        if self.mensaje_ganador:
            self.mensaje_ganador.destroy()
            self.mensaje_ganador = None