import unittest
#from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class TestChessExceptions(unittest.TestCase):

    def check_exception(self, exception_class, expected_message):
        with self.assertRaises(exception_class) as context:
            raise exception_class()
        self.assertEqual(str(context.exception), expected_message)

#Verifica que cuando se lanza la excepción InvalidMove, el mensaje asociado es "Movimieto de pieza invalido"   
    #def test_invalid_move_exception(self):
     #   with self.assertRaises(InvalidMove) as context:
      #      raise InvalidMove()
       # self.assertEqual(str(context.exception), "Movimieto de pieza invalido")

#Prueba la excepción InvalidTurn y su mensaje   
    #def test_invalid_turn_exception(self):
     #   with self.assertRaises(InvalidTurn) as context:
      #      raise InvalidTurn()
       # self.assertEqual(str(context.exception), "No puedes mover pieza de otro jugador")
    
if __name__ == "__main__":
    unittest.main()
