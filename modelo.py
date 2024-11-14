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
        valores = list(range(1, self.num_pares + 1)) * 2
        random.shuffle(valores)
        self.cartas = [Carta(valor) for valor in valores]

    def reiniciar(self):
        """Reinicia el juego creando un nuevo conjunto de cartas."""
        self.cartas_volteadas.clear()
        self.crear_cartas()

    def voltear_carta(self, indice):
        """Voltea una carta en la posición dada."""
        carta = self.cartas[indice]
        carta.voltear()
        if carta.visible:
            self.cartas_volteadas.append(carta)

    def es_par(self):
        """Verifica si las dos cartas volteadas forman un par."""
        if len(self.cartas_volteadas) == 2:
            carta1, carta2 = self.cartas_volteadas
            if carta1.valor == carta2.valor:
                carta1.encontrada = carta2.encontrada = True
                self.cartas_volteadas.clear()
                return True
            else:
                return False
        return None

    def todas_encontradas(self):
        """Comprueba si todas las cartas han sido encontradas."""
        return all(carta.encontrada for carta in self.cartas)
