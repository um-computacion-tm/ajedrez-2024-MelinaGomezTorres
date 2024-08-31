import unittest
from chess.board import Board
from chess.piezas.rook import Rook
from chess.piezas.knight import Knight
from chess.piezas.bishop import Bishop
from chess.piezas.queen import Queen
from chess.piezas.king import King
from chess.piezas.pawn import Pawn

#Secuencia de caracteres representa el tablero de ajedrez en su posición inicial
class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )
#Verifica que las piezas de ajedrez en la clase "Board" se inicien y coloquen correctamente en sus posiciones correspondientes en el tablero
    def test_get_piece(self):
        board = Board()
        rook = board.get_piece(0, 0)
        knight = board.get_piece(0, 1)
        bishop = board.get_piece(0, 2)
        queen = board.get_piece(0, 3)
        king = board.get_piece(0, 4)
        pawn = board.get_piece(1, 0)

        self.assertIsInstance(rook, Rook)
        self.assertIsInstance(knight, Knight)
        self.assertIsInstance(bishop, Bishop)
        self.assertIsInstance(queen, Queen)
        self.assertIsInstance(king, King)
        self.assertIsInstance(pawn, Pawn)

# Asegura que el tablero de ajedrez esté bien iniciado y que los casilleros que deberían estar vacíos no contienen ninguna pieza
    def test_empty_square(self):
        board = Board()
        empty_square = board.get_piece(4, 4)
        self.assertIsNone(empty_square)
                         
if __name__ == '__main__':
    unittest.main()
