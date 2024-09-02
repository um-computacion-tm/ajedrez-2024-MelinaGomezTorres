import unittest
from chess.piezas.rook import Rook

class TestRook(unittest.TestCase):

#Verifico la torre blanca (si quisiera testear solo el aspecto visual, sería suficiente con la pieza blanca)
    def test_str(self):
        rook_white = Rook("WHITE")
        self.assertEqual(
            str(rook_white),
            "♜",  # Símbolo para la torre blanca
        )
#Verifico también las torres negras para asegurar de que el código maneja todos los colores de manera correcta
        rook_black = Rook("BLACK")
        self.assertEqual(
            str(rook_black),
            "♖",  # Símbolo para la torre negra
        )

if __name__ == '__main__':
    unittest.main()

