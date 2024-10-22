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
        """
        Verifica la representación en cadena del tablero inicial.

        Compara la salida del método __str__ del tablero con
        la representación esperada del tablero en su posición inicial.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        board = Board() 
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "  ----------------\n"
                "0|♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ |0\n"
                "1|♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ |1\n"
                "2|. . . . . . . . |2\n"
                "3|. . . . . . . . |3\n"
                "4|. . . . . . . . |4\n"
                "5|. . . . . . . . |5\n"
                "6|♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ |6\n"
                "7|♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ |7\n"
                "  ----------------\n"
                "  0 1 2 3 4 5 6 7\n"
            )
        )
    def setUp(self):
        """
        Inicializa el tablero para cada prueba.

        Crea una nueva instancia de la clase Board que se usará
        en cada prueba para asegurarse de que cada prueba tenga
        un estado limpio.
        """
        self.board = Board() 
        
    def test_get_piece(self):
        """
        Verifica que las piezas de ajedrez se inicien y coloquen
        correctamente en sus posiciones correspondientes en el tablero.

        Comprueba que se pueden obtener las piezas de ajedrez en
        sus posiciones iniciales y asegura que son instancias de
        sus respectivas clases.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si alguna de las aserciones falla.
        """
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

    def test_empty_square(self):
        """
        Asegura que el tablero de ajedrez esté bien inicializado
        y que los casilleros que deberían estar vacíos no contienen
        ninguna pieza.

        Verifica que la casilla (4, 4) esté vacía y no contenga
        ninguna pieza.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        board = Board()
        empty_square = board.get_piece(4, 4)
        self.assertIsNone(empty_square)

    def test_get_piece_out_of_range(self):
        """
        Verifica que se lance una excepción al acceder a una posición
        fuera de límites.

        Intenta acceder a una posición fuera del tablero y asegura
        que se lanza la excepción OutOfBoard con el mensaje esperado.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si la aserción falla.
        """
        board = Board()  
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)  

        self.assertEqual(
            str(exc.exception),  # Compara el mensaje de la excepción directamente
        "La posicion indicada se encuentra fuera del tablero"
    )
        
    def test_capture_piece(self):
        """
        Verifica que una pieza se capture correctamente.

        Coloca una torre blanca y un peón negro en el tablero,
        mueve la torre a la posición del peón y verifica que
        la torre se haya movido correctamente y que la posición
        del peón ya esté vacía.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si alguna de las aserciones falla.
        """
        board = Board()

        # Se coloca una torre blanca en (0, 0) y un peón negro en (0, 1)
        board.set_piece(0, 0, Rook(color='WHITE', board=board))
        board.set_piece(0, 1, Pawn(color='BLACK', board=board))

        # La torre blanca se mueve a (0, 1) y se "come" al peón negro
        board.move(0, 0, 0, 1)

       # Verifica que la torre blanca esté en la nueva posición (0, 1)
        self.assertIsInstance(board.get_piece(0, 1), Rook)

        # Verifica que la pieza en la posición de origen (0, 0) ahora esté vacía
        self.assertIsNone(board.get_piece(0, 0))

        # Verifica que la pieza capturada ya no esté en el tablero
        self.assertNotIsInstance(board.get_piece(0, 1), Pawn)

    def test_move_to_empty_square(self):
        """
        Verifica que una pieza se mueva a una casilla vacía.

        Coloca una torre blanca en la posición (0, 0) y verifica
        que al moverla a una casilla vacía (0, 1) se haya movido
        correctamente.

        Retorna:
            None: Esta función no devuelve ningún valor, lanza una excepción
            si alguna de las aserciones falla.
        """
        board = Board()     
        board.set_piece(0, 0, Rook(color='WHITE', board=board))
        board.move(0, 0, 0, 1)

        # Verifica que la torre se haya movido correctamente
        self.assertIsInstance(board.get_piece(0, 1), Rook)
        self.assertIsNone(board.get_piece(0, 0))  # La casilla de origen ahora debe estar vacía

                         
if __name__ == '__main__':
    unittest.main()
