'''import unittest
from chess.piezas.bishop import Bishop
from chess.piezas.pawn import Pawn
#from chess.piece import Piece
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

    # Prueba el movimiento diagonal inferior derecha 
    def test_move_diagonal_bottom_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)

    # Coloca una pieza en (6, 6) para bloquear el movimiento
        pawn = Pawn("WHITE", board)
        board.set_piece(6, 6, pawn)

        possibles = bishop.possible_positions_dbr(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]  # El alfil debe detenerse en (5, 5) porque hay una pieza en (6, 6)
        )

    # Prueba el movimiento diagonal inferior izquierda 
    def test_move_diagonal_bottom_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)

        # Coloca una pieza enemiga en (6, 2) para bloquear el movimiento
        pawn = Pawn("BLACK", board)
        board.set_piece(6, 2, pawn)

        possibles = bishop.possible_positions_dbl(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2)],  # El alfil debe detenerse en (6, 2) donde está la pieza enemiga
        )

    # Prueba que el alfil no puede moverse horizontalmente (movimiento inválido)
    def test_invalid_horizontal_move(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        is_possible = bishop.valid_positions(4, 4, 4, 6)  # Intenta moverlo a (4, 6)
        self.assertFalse(is_possible, "El alfil no debería poder moverse horizontalmente")

    # Prueba que el alfil no puede moverse verticalmente (movimiento inválido)
    def test_invalid_vertical_move(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        is_possible = bishop.valid_positions(4, 4, 6, 4)  # Intenta moverlo verticalmente a (6, 4)
        self.assertFalse(is_possible, "El alfil no debería poder moverse verticalmente")

    # Prueba el movimiento con una pieza del mismo color bloqueando el camino
    def test_move_blocked_by_own_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        board.set_piece(2, 6, Pawn("WHITE", board))  # Coloca un peón blanco en el camino
        possibles = bishop.possible_positions_dtr(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)],  # El alfil debería moverse hasta (3, 5) y no más allá
        )

    # Prueba el movimiento con una pieza enemiga bloqueando el camino
    def test_move_blocked_by_enemy_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Coloca el alfil en (4, 4)
        board.set_piece(2, 6, Pawn("BLACK", board))  # Coloca un peón negro en el camino
        possibles = bishop.possible_positions_dtr(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6)],  # El alfil debería moverse hasta (2, 6), donde está el peón enemigo
        )

    # Prueba que el alfil no puede moverse fuera del tablero (movimiento inválido)
    def test_move_out_of_bounds(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(0, 0, bishop)  # Coloca el alfil en la esquina superior izquierda (0, 0)
        is_possible = bishop.valid_positions(0, 0, -1, 1)  # Intenta moverlo fuera del tablero
        self.assertFalse(is_possible, "El alfil no debería poder moverse fuera del tablero")




if __name__ == "__main__":
    unittest.main()'''