import unittest
from chess.piezas.rook import Rook
from chess.board import Board

class TestRook(unittest.TestCase):

#Verifica que el símbolo de la torre sea el correcto
    def test_str(self):
        rook_white = Rook("WHITE", None)
        self.assertEqual(str(rook_white), "♜")  # Símbolo para la torre blanca  
        rook_black = Rook("BLACK")
        self.assertEqual(str(rook_black), "♖")  # Símbolo para la torre negra

    def setUp(self):
#Configura el tablero y la torre blanca
        self.board = Board(for_test=True)  # Crea una instancia del tablero para pruebas.
        self.rook_white = Rook("WHITE", self.board) # Crea una torre blanca.
        self.board.set_piece(7, 0, self.rook_white) # Coloca la torre blanca en la posición (7, 0).
        self.clear_positions(6, 0, 5, 0) # Limpia las posiciones (6, 0) y (5, 0).

    def clear_positions(self, *positions):
#Limpia las posiciones del tablero estableciéndolas como vacías.
        for pos in positions:
            self.board.set_piece(pos, 0, None) # Establece cada posición como None.

    def test_rook_valid_moves(self):
#Verifica los movimientos válidos de la torre
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Movimiento hacia arriba.
        self.board.set_piece(5, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (5, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))  # No puede moverse sobre una aliada.
        self.board.set_piece(6, 0, Rook("BLACK", self.board))   # Coloca una torre negra en (6, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 6, 0))   # Puede capturar la negra.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 8, 0))  # Fuera de límites.

    def test_rook_cannot_jump_over_ally(self):
#Verifica que la torre no puede saltar sobre piezas aliadas
        self.board.set_piece(6, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (6, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 5, 0))   # No puede moverse a (5, 0).

    def test_rook_can_capture_enemy(self):
#Verifica que la torre puede capturar piezas enemigas
        self.board.set_piece(5, 0, Rook("BLACK", self.board))  # Coloca una torre negra en (5, 0).
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 5, 0))  # Puede capturar.

    def test_rook_cannot_move_diagonally(self):
#Verifica que la torre no puede moverse en diagonal
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 6, 1))  # Movimiento diagonal inválido.

    def test_rook_moves_until_obstacle(self):
#Verifica que la torre se detiene al encontrar un obstáculo
        for i in range(6, 0, -1):
            self.board.set_piece(i, 0, None) # Limpia las posiciones en la columna.
        self.assertTrue(self.rook_white.__valid_positions__(7, 0, 0, 0))   # Puede moverse a (0, 0).
        self.board.set_piece(3, 0, Rook("WHITE", self.board))  # Coloca una torre blanca en (3, 0).
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 0, 0))  # No puede moverse a (0, 0) por obstáculo.

    def test_rook_move_out_of_bounds(self):
#Verifica movimientos fuera del tablero (fila y columna)
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 9, 0))  # Fuera de límites en fila.
        self.assertFalse(self.rook_white.__valid_positions__(7, 0, 7, -1))  # Fuera de límites en columna.



        


#Prueba el movimiento vertical descendente (hacia abajo) de la torre.
    #def test_move_vertical_desc(self):
     #   board = Board()
      #  rook = Rook("WHITE", board)
       # possibles = rook.possible_positions_vd(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(5, 1)]
        #)

#Prueba el movimiento vertical ascendente (hacia arriba) de la torre.
    #def test_move_vertical_asc(self):
     #   board = Board()
      #  rook = Rook("WHITE", board)
       # possibles = rook.possible_positions_va(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(3, 1), (2, 1), (1, 1)]
        #)
#Prueba el movimiento vertical descendente de la torre cuando hay una pieza propia (del mismo color) en el camino.
    #def test_move_vertical_desc_with_own_piece(self):
     #   board = Board()
      #  board.set_piece(6, 1, Pawn("WHITE", board))
       # rook = Rook("WHITE", board)
        #board.set_piece(4, 1, rook)
        #possibles = rook.possible_positions_vd(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(5, 1)]
        #)
#Prueba el movimiento vertical descendente de la torre cuando hay una pieza contraria en el camino.
    #def test_move_vertical_desc_with_not_own_piece(self):
     #   board = Board()
      #  board.set_piece(6, 1, Pawn("BLACK", board))
       # rook = Rook("WHITE", board)
        #board.set_piece(4, 1, rook)
        #possibles = rook.possible_positions_vd(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(5, 1), (6, 1)]
        #)

#Prueba el movimiento horizontal hacia la derecha de la torre.
    #def test_move_horizontal_right(self):
     #   board = Board()
      #  rook = Rook("WHITE", board)
       # board.set_piece(4, 1, rook)  # Se coloca la torre en (4, 1)
        #possibles = rook.possible_positions_hr(4, 1)
        #self.assertEqual(
         #   possibles,
        #[(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]  # Posiciones válidas
    #)

#Prueba el movimiento horizontal hacia la izquierda de la torre.
    #def test_move_horizontal_left(self):
     #   board = Board()
      #  rook = Rook("WHITE", board)
       # board.set_piece(4, 5, rook)  # Se coloca la torre en (4, 5)
        #possibles = rook.possible_positions_hl(4, 5)
        #self.assertEqual(
         #   possibles,
        #[(4, 4), (4, 3), (4, 2), (4, 1), (4, 0)]  # Incluye la columna 0
    #)

#Prueba el movimiento horizontal hacia la derecha de la torre cuando hay una pieza propia en el camino.        
    #def test_move_horizontal_right_with_own_piece(self):
     #   board = Board()
      #  board.set_piece(4, 3, Pawn("WHITE", board))
       # rook = Rook("WHITE", board)
        #board.set_piece(4, 1, rook)
        #possibles = rook.possible_positions_hr(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(4, 2)]
        #)
        
#Prueba el movimiento horizontal hacia la derecha de la torre cuando hay una pieza contraria en el camino.
    #def test_move_horizontal_right_with_not_own_piece(self):
     #   board = Board()
      #  board.set_piece(4, 3, Pawn("BLACK", board))
       # rook = Rook("WHITE", board)
        #board.set_piece(4, 1, rook)
        #possibles = rook.possible_positions_hr(4, 1)
        #self.assertEqual(
         #   possibles,
          #  [(4, 2), (4, 3)]
        #)

    #def test_move_diagonal_desc(self):
     #   board = Board()
      #  rook = board.get_piece(col=0, row=0)
       # is_possible = rook.valid_positions(
# Intentar moverse en diagonal desde (0, 0) hasta (1, 1)
        #    from_row=0,
         #   from_col=0,
          #  to_row=1,
           # to_col=1,
        #)
# Verifica que el movimiento diagonal no es válido
        #self.assertFalse(is_possible, "La torre no debería poder moverse en diagonal")


if __name__ == '__main__':
    unittest.main() 
























    