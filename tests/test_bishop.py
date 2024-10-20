import unittest
from chess.piezas.bishop import Bishop
from chess.board import Board


class TestBishop(unittest.TestCase):

    # Verifica que el símbolo del alfil sea el correcto según el color
    def test_str(self):
        self.assertEqual(str(self.bishop_white),"♝")   # Símbolo para el alfil blanco
        bishop_black = Bishop("BLACK")
        self.assertEqual(str(bishop_black),"♗")        # Símbolo para el alfil negro

    def setUp(self):
        # Configura el tablero y el alfil blanco antes de cada prueba
        # Crea un tablero vacío configurado para pruebas
        self.board = Board(for_test=True) 
        self.bishop_white = Bishop("WHITE", self.board)    # Crea un alfil blanco
        self.board.set_piece(4, 4, self.bishop_white)   # Coloca el alfil blanco en la posición (4, 4) en el tablero
    
    def test_bishop_valid_moves(self):
        # Verifica los movimientos válidos del alfil
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 5))  # Movimiento válido diagonal (hacia arriba a la derecha)
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 3, 3))  # Movimiento válido diagonal (hacia abajo a la izquierda)
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 4))  # Movimiento no válido (horizontal)
        # Verifica que el alfil no puede saltar sobre la pieza aliada (no puede moverse a (2, 2))
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 4, 5))  # Movimiento no válido (vertical)

    def test_bishop_cannot_jump_over_ally(self):
        # Verifica que el alfil no puede saltar sobre piezas aliadas
        self.board.set_piece(3, 3, Bishop("WHITE", self.board))  # Pone un alfil aliado en el camino
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 2, 2))  # No puede moverse

    def test_bishop_can_capture_enemy(self):
        # Verifica que el alfil puede capturar piezas enemigas
        self.board.set_piece(5, 5, Bishop("BLACK", self.board))  # Pone un alfil enemigo
        # Verifica que el alfil blanco puede moverse a la posición (5, 5) para capturar al enemigo
        self.assertTrue(self.bishop_white.valid_positions_in_bishop(4, 4, 5, 5))  # Movimiento válido (captura)

    def test_bishop_moves_until_obstacle(self):
        # Verifica que el alfil se detiene al encontrar un obstáculo
        self.board.set_piece(6, 6, Bishop("WHITE", self.board))  # Pone un alfil aliado que obstruye
        # Verifica que el alfil no puede moverse más allá de la pieza aliada (no puede moverse a (7, 7))
        self.assertFalse(self.bishop_white.valid_positions_in_bishop(4, 4, 7, 7))  # No puede moverses

'''    # Prueba el movimiento diagonal superior derecha 
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
        self.assertFalse(is_possible, "El alfil no debería poder moverse fuera del tablero")'''




if __name__ == "__main__":
    unittest.main()





