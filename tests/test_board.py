import unittest
from chess.board import Board
from chess.piezas.rook import Rook
from chess.piezas.knight import Knight
from chess.piezas.bishop import Bishop
from chess.piezas.queen import Queen
from chess.piezas.king import King
from chess.piezas.pawn import Pawn
from chess.exceptions import OutOfBoard

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

    def test_move(self):
        board = Board()  
        rook = Rook(color='BLACK') 

        board.set_piece(0, 0, rook)  # Coloca la torre negra en la posición inicial

    # Mueve la torre de (0,0) a (0,1)
        board.move(from_row=0, from_col=0, to_row=0, to_col=1)

    # Verifica que la torre esté en la nueva posición
        self.assertIsInstance(board.get_piece(0, 1), Rook)

    # Verifica que la representación del tablero sea correcta
        self.assertEqual(
            str(board),
        (
            " ♖♗♕♔♗♘♖\n"
            "♙♙♙♙♙♙♙♙\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♟♟♟♟♟♟♟♟\n"
            "♜♞♝♛♚♝♞♜\n"
        )
    )
    def test_get_piece_out_of_range(self):
        board = Board()  
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)  # Intenta acceder a una posición fuera de los límites

        self.assertEqual(
            str(exc.exception),  # Compara el mensaje de la excepción directamente
        "La posicion indicada se encuentra fuera del tablero"
    )
        
    def test_capture_piece(self):
        board = Board()

        # Se coloca una torre blanca en (0, 0) y un peón negro en (0, 1)
        board.set_piece(0, 0, Rook(color='WHITE'))
        board.set_piece(0, 1, Pawn(color='BLACK'))

        # La torre blanca se mueve a (0, 1) y se "come" al peón negro
        board.move(0, 0, 0, 1)

       # Verifica que la torre blanca esté en la nueva posición (0, 1)
        self.assertIsInstance(board.get_piece(0, 1), Rook)

        # Verifica que la pieza en la posición de origen (0, 0) ahora esté vacía
        self.assertIsNone(board.get_piece(0, 0))

        # Verifica que la pieza capturada ya no esté en el tablero
        self.assertNotIsInstance(board.get_piece(0, 1), Pawn)




    
                         
if __name__ == '__main__':
    unittest.main()
