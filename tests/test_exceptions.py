import unittest
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class TestChessExceptions(unittest.TestCase):

#Captura la excepción lanzada y verifica que el mensaje asociado a la excepción coincide con el mensaje esperado
    def check_exception(self, exception_class, expected_message):
        with self.assertRaises(exception_class) as context:
            raise exception_class()
        self.assertEqual(str(context.exception), expected_message)

#Verifica que cuando se lanza la excepción InvalidMove, el mensaje sea el esperado
    def test_invalid_move_exception(self):
        self.check_exception(InvalidMove, "Movimieto de pieza invalido")

#Garantiza que la excepción InvalidTurn está correctamente implementada con el mensaje correspondiente
    def test_invalid_turn_exception(self):
        self.check_exception(InvalidTurn, "No puedes mover pieza de otro jugador")

#Confirma que EmptyPosition lanza el mensaje correcto cuando la excepción es invocada
    def test_empty_position_exception(self):
        self.check_exception(EmptyPosition, "La posicion esta vacia")

#Verifica que la excepción OutOfBoard está implementada correctamente y lanza el mensaje adecuado   
    def test_out_of_board_exception(self):
        self.check_exception(OutOfBoard, "La posicion indicada se encuentra fuera del tablero")
    
if __name__ == "__main__":
    unittest.main()
