import random

class Carta:
    def __init__(self, valor):
        self.valor = valor
        self.visible = False
        self.encontrada = False

    def voltear(self):
        """Cambia el estado de la carta (boca arriba/boca abajo)."""
        if not self.encontrada:
            self.visible = not self.visible

class JuegoMemoria:
    def __init__(self, num_pares):
        self.num_pares = num_pares
        self.cartas = []
        self.cartas_volteadas = []
        self.crear_cartas()

    def crear_cartas(self):
        """Crea una lista de cartas con pares de valores y las baraja."""
        valores = list(range(1, self.num_pares + 1)) * 2  # Crear pares de valores
        random.shuffle(valores)
        self.cartas = [Carta(valor) for valor in valores]
