class InvalidMove(Exception):
    """
    Excepción que se lanza cuando se intenta realizar un movimiento inválido de una pieza en el juego de ajedrez.
    """
    message = "Movimieto de pieza invalido"
    
    def __str__(self):
        """
        Devuelve el mensaje de error asociado a la excepción.

        Retorna:
            str: Mensaje que describe el error.

        Realiza:
            - Retorna un mensaje estándar indicando que el movimiento es inválido.
        """
        return self.message

class InvalidTurn(InvalidMove):
    """
    Excepción que se lanza cuando un jugador intenta mover una pieza que no le pertenece.
    """
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    """
    Excepción que se lanza cuando se intenta mover desde una posición que no contiene ninguna pieza.
    """
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    """
    Excepción que se lanza cuando se intenta acceder a una posición que está fuera del tablero.
    """
    message = "La posicion indicada se encuentra fuera del tablero"


    