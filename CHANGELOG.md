# CHANGELOG

# [0.48] - 09 / 10 / 2024 - Cambios en bishop

### Changed

- Simplificación de la lógica del movimiento del alfil

# [0.47] - 05 / 10 / 2024 - Últimos test para rook

### Added

- Test de que la torre se detiene al encontrar un obstáculo
- Test de movimientos fuera del tablero

# [0.46] - 04 / 10 / 2024 - Más test para rook

### Added

- Agregados más test para rook

# [0.45] - 03 / 10 / 2024 - Cambios en rook y pruebas agregadas para test_rook

### Changed

- Cambios en el método str de rook

### Added

- Configuración del tablero y la torre blanca (método setUp)
- Test para limpiar las posiciones del tablero
- Test de movimientos válidos de la torre

# [0.44] - 02 / 10 / 2024 - Cambios en rook 

### Changed

- Simplificación de la lógica del movimiento de la torre

# [0.43] - 30 / 09 / 2024 - Movimientos en piece

### Added

- Cálculo de movimientos en todas las direcciones 

# [0.42] - 29 / 09 / 2024 - Cambios en el archivo piece

### Changed

- Cambios en el código de piece.py para una mejor identificación de las piezas

# [0.41] - 28 / 09 / 2024 - Test para exceptions nuevo

### Added

- Subido test para las excepciones con sus mensajes respectivos

# [0.40] - 27 / 09 / 2024 - Modificaciones en test_exceptions

### Changed

- Modificación para evitar repeticiones

# [0.39] - 26 / 09 / 2024 - Test para exceptions

### Added

- Creación de test en exceptions para InvalidMove y InvalidTurn

## [0.38] - 25 / 09 / 2024 - Modificaciones en board

### Changed

- Modificaciones en el código de las posiciones para evitar repetición en el tablero

## [0.37] - 24 / 09 / 2024 - Test para bishop

### Added

- Subido test para comprobar que el alfíl no se mueva fuera del tablero

## [0.36] - 23 / 09 / 2024 - Test para bishop

### Added

- Subido test para piezas del mismo color y pieza enemiga bloqueando el camino

## [0.35] - 22 / 09 / 2024 - Pruebas para movimientos en test_bishop

### Added

- Subido test para movimiento inferior izquierda
- Subido test para movimiento invalido para vertical y horizontal

## [0.34] - 21 / 09 / 2024 - Correción de movimientos en bishop

### Fixed

- Correción de movimientos dtr, dtl y dbl en bishop.py

## [0.33] - 20 / 09 / 2024 - Correción de movimientos y test para bishop

### Fixed

- Correción del movimiento dbr en bishop.py

### Added

- Subido test para movimiento inferior derecha en test_bishop.py

## [0.32] - 19 / 09 / 2024 - Tests restantes para bishop

### Added

- Subido test para el movimiento diagonal superior izquierda

## [0.31] - 18 / 09 / 2024 - Tests para bishop

### Added

- Subido test para símbolos correctos
- Movimiento diagonal superior derecha

## [0.30] - 16 / 09 / 2024 - Movimiento horizontal y diagonal en test_rook

### Added

- Subido test para movimiento horizontal frente a una pieza
- Subido test movimiento diagonal es invalido

## [0.29] - 15 / 09 / 2024 - Movimiento horizontal para la torre

### Added

- Subidos movimientos horizontales para la torre en rook.py y test_rook.py

## [0.28] - 14 / 09 / 2024 - Actualización del init para las piezas

### Changed

- Actualizar __init__ en Piece para board.py en todas las piezas 
- Incluir self como segundo argumento en piezas


## [0.27] - 13 / 09 / 2024 - Código restante para movimientos en bishop

### Added

- Subidos movimientos diagonales hacia abajo para bishop.py

## [0.26] - 12 / 09 / 2024 - Movimientos para bishop

### Added

- Subidos movimientos diagonales hacia arriba para bishop.py

## [0.25] - 11 / 09 / 2024 - Cambios en rook y test_rook

### Changed

- Método para posibles posiciones cambiado
- Cambios en movimiento vertical ascendente y descendente

## [0.24] - 09 / 09 / 2024 - Test para board restante

### Added

- Subido el resto del código para comer una pieza

## [0.23] - 08 / 09 / 2024 - Test para board

### Added

- Subido parte de test para comer una pieza 

## [0.22] - 06 / 09 / 2024 - Test para chess

### Added

- Subido test para un movimiento invalido en test_chess.py

## [0.21] - 05 / 09 / 2024 - Test echos en clase

### Added

- Subidos los test hechos en clases con el resto de las piezas en el tablero

### Changed

- Cambios en el archivo exceptions.py

## [0.20] - 04 / 09 / 2024 - Test del chess

### Added

- Test para verificar que el turno no cambie cuando no debe

## [0.19] - 02 / 09 / 2024 -  Configuración para rook

### Added

- Agregado método init a rook.py
- Agregado test inicial para test_rook.py

## [0.18] - 01 / 09 / 2024 - Símbolos para las piezas 

### Added

- Simbolos correspondientes para las piezas

### Fixed

- Arreglos para método str en las piezas

## [0.17] - 31 / 08 / 2024 - Piezas restantes con su posición indicadas

### Added

- Verificación de las piezas en su posición correspondiente en test_board.py para queen, king y pawn

### Fixed - Exceptions.py

-Ligeros arreglos en exceptions.py

## [0.16] - 30 / 08 / 2024 - Piezas en su posición correcta

### Added

- Verificación de las piezas en su posición correspondiente en test_board.py para rook, knight y bishop

## [0.15] - 29 / 08 / 2024 - Carácteres del ajedres + Test tablero

### Added

- Método para asegurar que los casilleros vacios no tengan piezas en test_board.py
- Tablero bien inicializado en test_board.py
- Agregados los carácteres para cada pieza

## [0.14] - 28 / 08 / 2024 - Configuración piece.py

### Added

- Método str

## [0.13] - 27 / 08 / 2024 - Configuración del test_chess

### Added

- Método para juego en marcha

## [0.12] - 24 / 08 / 2024 - Configuración inicial

### Added

- Configuración inicial para el peón en el archivo board.py

## [0.11] - 23 / 08 / 2024 - Configuración inicial

### Added

- Configuración inicial para el rey y la reina en el archivo board.py

## [0.10] - 22 / 08 / 2024 - Configuración inicial

### Added

- Configuración inicial para el caballo y el alfíl en el archivo board.py

## [0.9] - 21 / 08 / 2024 - Configuración inicial

### Added

- Configuración inicial de la torre en el archivo board.py

## [0.8] - 20 / 08 / 2024 - Archivos en clase

### Added

- Subidos los archivos realizados en clase

## [0.7] - 19 / 08 / 2024 - Test cambio de turno cambiado

### Added

- Subido cambios en el test para secuencia de turnos en el ajedrez en el archivo test_chess.py

## [0.6] - 18 / 08 / 2024 - Test cambio de turno

### Added

- Subido test para secuencia de turnos en el ajedrez en el archivo test_chess.py

## [0.5] - 17 / 08 / 2024 - Agregadas más pruebas

### Added

- Subidos más test para chess.py

## [0.4] - 16 / 08 / 2024 - Coordenadas

### Changed

- Coorección de coordenadas para el archivo cli.py

## [0.3] - 15 / 08 / 2024 - Test provisional

### Added

- Subido un test provisional para el archivo chess.py

## [0.2] - 14 / 08 / 2024 - Archivos Principales 

### Added

- Subidos los archivos principales al repo 

## [0.1] - 11 / 08 / 2024 - Archivos Generales

### Added

- Subidos los archivos generales al repo
