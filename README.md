# ajedrez-2024-MelinaGomezTorres

Proyecto de ajedrez diseñado por la alumna Melina Abril Gomez Torres.

# Legajo
**63211**



# CircleCi
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-MelinaGomezTorres/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-MelinaGomezTorres/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/f12ad0387fdb8ca012f7/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-MelinaGomezTorres/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/f12ad0387fdb8ca012f7/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-MelinaGomezTorres/test_coverage)

---

# ♛ Descripción:

Este proyecto tiene como objetivo desarrollar un juego de Ajedrez utilizando el lenguaje de programación Python, siguiendo las reglas y mecánicas del juego descritas en el artículo de Wikipedia sobre Ajedrez. El juego se ejecutará en una interfaz de consola, permitiendo a los usuarios disfrutar de partidas de Ajedrez con todas las funcionalidades esenciales.

---

##  Requisitos:

- Python 3.x instalado en el sistema.
- Docker para ejecutar el juego en un contenedor. Documentación oficial de Docker para su instalación: [Docker](https://docs.docker.com/get-started/get-docker/).
- Dependencias.

---

##  Funcionalidades:

- **Tablero.**
- **Piezas de Ajedrez.**
- **Validación de Movimientos.**
- **Interfaz de Línea de Comandos (CLI).**
- **Finalización de la Partida.**
- **Cambios de turnos.**
- **Pruebas Unitarias.**
- **Compatibilidad con Docker.**

---

## Modo de Jugar:

Cada jugador realiza sus respectivos movimientos para cada pieza hasta que:

- Se decide terminar la partida ingresando la palabra **'EXIT'**.
- Ambos jugadores deciden declarar un empate.
- Uno de los jugadores se queda sin piezas.

---

##  Instrucciones para Ejecutar:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/um-computacion-tm/ajedrez-2024-MelinaGomezTorres.git
   ```

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Inicia el juego**:

   ```bash
   python3 -m chess.cli
   ```

---

##  Docker:

1. **Construcción de la imagen Docker**:

   ```bash
   docker buildx build -t ajedrez-2024-melinagomeztorres .
   ```

2. **Correr el contenedor y ejecutar las respectivas pruebas**:

   ```bash
   docker run -i ajedrez-2024-melinagomeztorres
   ```

---

