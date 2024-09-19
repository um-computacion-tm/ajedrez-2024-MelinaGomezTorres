import unittest
from chess.piezas.bishop import Bishop
#from chess.piezas.pawn import Pawn
from chess.piece import Piece
from chess.board import Board


class TestBishop(unittest.TestCase):

    # Verifica que el símbolo del alfil sea el correcto según el color
    def test_str(self):
        bishop_white = Bishop("WHITE", None)
        bishop_black = Bishop("BLACK", None)
        self.assertEqual(
            str(bishop_white),
            "♝",  # Símbolo para el alfil blanco
        )
        self.assertEqual(
            str(bishop_black),
            "♗",  # Símbolo para el alfil negro
        )

    # Prueba el movimiento diagonal superior derecha 
    def test_move_diagonal_top_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        possibles = bishop.possible_positions_dtr(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]  # Posiciones válidas en la diagonal superior derecha
        )

    # Prueba el movimiento diagonal superior izquierda 
    def test_move_diagonal_top_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        possibles = bishop.possible_positions_dtl(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1)]  # Posiciones válidas en la diagonal superior izquierda
        )


        


    
    



if __name__ == "__main__":
    unittest.main()