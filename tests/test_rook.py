import unittest
from chess.piezas.rook import Rook
from chess.piezas.pawn import Pawn
from chess.board import Board

class TestRook(unittest.TestCase):

#Verifico +la torre blanca (si quisiera testear solo el aspecto visual, sería suficiente con la pieza blanca)
    def test_str(self):
        rook_white = Rook("WHITE", None)
        self.assertEqual(
            str(rook_white),
            "♜",  # Símbolo para la torre blanca        
        )

#Verifico también las torres negras para asegurar de que el código maneja todos los colores de manera correcta
#        rook_black = Rook("BLACK")
 #       self.assertEqual(
  #          str(rook_black),
   #         "♖",  # Símbolo para la torre negra
    #    )
            

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

if __name__ == '__main__':
    unittest.main()
    