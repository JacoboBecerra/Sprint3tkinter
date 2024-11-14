class ControladorJuego:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def voltear_carta(self, indice):
        """Lógica para voltear una carta y actualizar la vista."""
        if len(self.modelo.cartas_volteadas) < 2:
            self.modelo.voltear_carta(indice)
            carta = self.modelo.cartas[indice]
            if carta.visible:
                self.vista.mostrar_valor_carta(indice, carta.valor)

            if len(self.modelo.cartas_volteadas) == 2:
                es_par = self.modelo.es_par()
                if es_par is False:
                    # Esperar un segundo antes de ocultar las cartas que no son pareja
                    self.vista.botones[indice].after(1000, self.ocultar_cartas_no_pareja)
                elif self.modelo.todas_encontradas():
                    self.vista.mostrar_mensaje_ganador()

    def ocultar_cartas_no_pareja(self):
        """Oculta las cartas que no son pareja después de un tiempo."""
        for carta in self.modelo.cartas_volteadas:
            indice = self.modelo.cartas.index(carta)
            self.vista.ocultar_valor_carta(indice)
        self.modelo.cartas_volteadas.clear()

    def reiniciar_juego(self):
        """Reinicia el juego reseteando el modelo y la vista."""
        self.modelo.reiniciar()
        self.vista.reiniciar_tablero()
