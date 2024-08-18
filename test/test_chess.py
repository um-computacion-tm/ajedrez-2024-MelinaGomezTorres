#Importo el módulo y la clase "Chess" desde la carpeta con el mismo nombre
#Importo más clases (Board y Piece)
import unittest
from chess.chess import Chess
from chess.board import Board
from chess.piece import Piece
#Creo la clase correspondiente para este test 
# Entro de setUp (se ejecuta automáticamente antes de cada prueba para asegurar que estas no se repitan)
# Creo una nueva instancia del juego de ajedrez (self.game = Chess())

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.__game__ = Chess()

#Verifica que el turno incial sea de las piezas blancas, casa contrario se mostrará un mensaje indicando el error
    def test_initial_turn(self):
        self.assertEqual(self.__game__.turn, "WHITE" , "El turno inicial debe ser de las piezas blancas")

#Me aseguro de que el turno cambia de "WHITE" a "BLACK" después de un movimiento.
    def test_turn_sequence(self):
        self.__game__.move(0, 0, 1, 0)  # Mueve una pieza
        self.assertEqual(self.__game__.turn, "BLACK", "El turno debe cambiar a negro después de un movimiento")


if __name__ == '__main__':
    unittest.main()
