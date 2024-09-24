#Importo el módulo y la clase "Chess" desde la carpeta con el mismo nombre
#Importo más clases (Board y Piece)
import unittest
from chess.chess import Chess
#from chess.board import Board
# from chess.piece import Piece
#Creo la clase correspondiente para este test 
# Entro de setUp (se ejecuta automáticamente antes de cada prueba para asegurar que estas no se repitan)
# Creo una nueva instancia del juego de ajedrez (self.game = Chess())

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.__game__ = Chess()

# Asegura que el juego esté en marcha cuando se llama al método is_playing
    def test_is_playing(self):
        self.assertTrue(self.__game__.is_playing(), "El juego debería estar en curso")

#Verifica que el turno incial sea de las piezas blancas, casa contrario se mostrará un mensaje indicando el error
    def test_initial_turn(self):
        self.assertEqual(self.__game__.turn, "WHITE" , "El turno inicial debe ser de las piezas blancas")

#Me aseguro de que el turno cambia de "WHITE" a "BLACK" después de un movimiento.
    def test_turn_sequence(self):
         self.__game__.move(0, 0, 1, 0)  # Mueve una pieza
         self.assertEqual(self.__game__.turn, "BLACK", "El turno debe cambiar a negro después de un movimiento")

#Me aseguro que después de mover una pieza negra, siga una pieza blanca
         self.__game__.move(7, 0, 6, 0)  
         self.assertEqual(self.__game__.turn, "WHITE", "El turno debe cambiar a blanco después de otro movimiento")

#Se compara el turno actual con el turno guardado antes de la acción. Si son iguales, el test pasa, sino, el test falla con el mensaje especificado
    def test_turn_unchanged(self):
        initial_turn = self.__game__.turn
        self.__game__.is_playing()  # Acción que no debería cambiar el turno
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar al llamar a is_playing()")

#Verifica que el turno de los jugadores no cambia cuando se realiza un movimiento inválido
    def test_turn_unchanged_after_invalid_move(self):
        initial_turn = self.__game__.turn
        try:
            self.__game__.move(10, 10, 11, 11)  # Movimiento inválido de ejemplo
        except Exception:
            pass
        self.assertEqual(self.__game__.turn, initial_turn, "El turno no debería cambiar después de un movimiento inválido")






                         
if __name__ == '__main__':
    unittest.main()
