import unittest
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class TestChessExceptions(unittest.TestCase):
    """Clase de prueba para las excepciones del ajedrez."""

    def check_exception(self, exception_class, expected_message):
        """
        Captura la excepción lanzada y verifica que el mensaje asociado
        a la excepción coincide con el mensaje esperado.

        :param exception_class: La clase de excepción que se espera lanzar.
        :param expected_message: El mensaje esperado de la excepción.
        :raises exception_class: Lanza la excepción para verificarla.
        :return: None
        """
        with self.assertRaises(exception_class) as context:
            raise exception_class() 
        self.assertEqual(str(context.exception), expected_message)

    def test_invalid_move_exception(self):
        """
        Verifica que cuando se lanza la excepción InvalidMove, el mensaje
        sea el esperado.

        :return: None
        """
        self.check_exception(InvalidMove, "Movimieto de pieza invalido")

    def test_invalid_turn_exception(self):
        """
        Garantiza que la excepción InvalidTurn está correctamente
        implementada con el mensaje correspondiente.

        :return: None
        """
        self.check_exception(InvalidTurn, "No puedes mover pieza de otro jugador")

    def test_empty_position_exception(self):
        """
        Confirma que EmptyPosition lanza el mensaje correcto cuando la
        excepción es invocada.

        :return: None
        """
        self.check_exception(EmptyPosition, "La posicion esta vacia")

    def test_out_of_board_exception(self):
        """
        Verifica que la excepción OutOfBoard está implementada correctamente
        y lanza el mensaje adecuado.

        :return: None
        """
        self.check_exception(OutOfBoard, "La posicion indicada se encuentra fuera del tablero")
    
if __name__ == "__main__":
    unittest.main()
