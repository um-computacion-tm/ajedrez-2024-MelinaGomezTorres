# Excepción base para movimientos inválidos de piezas en el juego de ajedrez.
class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

# Excepción para indicar que se ha intentado mover una pieza del jugador equivocado.
class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

# Excepción para indicar que se ha intentado mover desde una posición vacía.
class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

# Excepción para indicar que se ha intentado acceder a una posición fuera de los límites del tablero.
class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"


    