class Piece:
    def __init__(self, color ,board):
        self.__color__ = color
        self.__board__ = board

#Cambio de codigo para que las piezas sean más visuales y fáciles de identificar en el juego
    def __str__(self):
        #Obtiene el símbolo de la pieza según su color
        return getattr(self, f"__{self.__color__.lower()}_symbol__", "")
    
    #Anterior
    #def __str__(self):
     #   return f"{self.__class__.__name__} ({self.__color__})"
        
    def get_color(self):
        return self.__color__

    
    