# novel-visual-interface

Este proyecto es una interfaz de menú para una novela visual desarrollada en Python utilizando la librería Pygame. La aplicación incluye un menú principal con opciones para iniciar o cargar un juego, un menú de opciones para ajustar la configuración del volumen, y una animación de transición entre los menús.

## Funcionalidades

- **Menú Principal**: Permite iniciar un juego, cargar un juego, acceder a las opciones o salir de la aplicación.
- **Menú de Opciones**: Permite ajustar el volumen y regresar al menú principal.
- **Configuración de Volumen**: Incluye un slider para ajustar el volumen de la música de fondo.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/staFF6773/novel-visual-interface.git
    ```

2. **Instala Pygame**:
    ```bash
    pip install pygame
    ```

3. **Coloca los recursos**:
   - Asegúrate de que las imágenes y sonidos necesarios estén en las rutas especificadas en el código (`Sprite/background/menu_background.png`, `Sprite/sounds/click-button-131479.mp3`, etc.).

## Uso

1. **Ejecuta el archivo principal**:
    ```bash
    python main.py
    ```

2. **Navega por los menús**:
   - En el menú principal, puedes seleccionar entre "Iniciar Juego", "Cargar Juego", "Opciones" y "Salir".
   - En el menú de opciones, puedes ajustar el volumen utilizando el slider y volver al menú principal.

## Estructura del Código

- `main.py`: Archivo principal que contiene la lógica de la aplicación y los menús.
- `Sprite/background/menu_background.png`: Imagen de fondo para el menú.
- `Sprite/sounds/click-button-131479.mp3`: Sonido para el hover en los botones.
- `Sprite/sounds/BGM Pack 1 MP3/frozen_winter.mp3`: Música de fondo del juego.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Envía tus cambios a tu repositorio (`git push origin nueva-caracteristica`).
5. Crea un pull request desde tu repositorio al principal.
