
class Piece:
    def __init__(self, color ,board):
        self.__color__ = color
        self.__board__ = board

#El método `__str__` convierte un objeto en una cadena de texto que describe el objeto
#(Se muestra el nombre de la clase y el color de la pieza, lo que facilita la impresión y depuración del objeto)
    def __str__(self):
        return f"{self.__class__.__name__} ({self.__color__})"
    
    def get_color(self):
        return self.__color__