#Importo el módulo y la clase "chess" desde la carpeta con el mismo nombre
import unittest
from chess.chess import Chess

#Creo la clase correspondiente para este test 
# Entro de setUp (se ejecuta automáticamente antes de cada prueba para asegurar que estas no se repitan)
# Creo una nueva instancia del juego de ajedrez (self.game = Chess())

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.game = Chess()

if __name__ == '__main__':
    unittest.main()
