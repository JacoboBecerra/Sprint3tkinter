class RegistroPartidas:
    archivo = "registro_partidas.txt"

    @staticmethod
    def registrar_partida(nombre, dificultad, resultado):
        """Registra una partida en un archivo."""
        with open(RegistroPartidas.archivo, "a") as f:
            f.write(f"{nombre} | {dificultad} | {'Ganó' if resultado else 'Perdió'}\n")

    @staticmethod
    def obtener_registro():
        """Devuelve el registro de partidas en formato de lista."""
        try:
            with open(RegistroPartidas.archivo, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []
