import pygame
import sys

# Inicialización de Pygame y del mixer para el sonido
pygame.init()
pygame.mixer.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menú Principal - Novela Visual")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (70, 70, 70)
HOVER_COLOR = (100, 100, 100)
TEXT_COLOR = WHITE
TITLE_COLOR = (255, 204, 0)
SLIDER_COLOR = (150, 150, 150)
SLIDER_HOVER_COLOR = (200, 200, 200)
SLIDER_FILL_COLOR = (0, 128, 255)

# Fuente para los textos
title_font = pygame.font.Font(None, 80)
font = pygame.font.Font(None, 40)
info_font = pygame.font.Font(None, 30)

# Cargar imágenes (Fondo)
background = pygame.image.load('Sprite/background/menu_background.png')
#studio_background = pygame.image.load('Sprite/background/black.png')  # Imagen de la pantalla del estudio

# Cargar sonidos
hover_sound = pygame.mixer.Sound('Sprite/sounds/click-button-131479.mp3')
pygame.mixer.music.load('Sprite/sounds/BGM Pack 1 MP3/frozen_winter.mp3')  # Cargar el archivo de música

def draw_rounded_button(text, x, y, width, height, hover=False):
    color = HOVER_COLOR  if hover else BUTTON_COLOR
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect, border_radius=15)  # Botón redondeado
    
    # Renderizar texto en el botón
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def draw_title(text, x, y):
    title_surface = title_font.render(text, True, TITLE_COLOR)
    title_rect = title_surface.get_rect(center=(x, y))
    screen.blit(title_surface, title_rect)

def animate_transition(target_y, duration):
    start_time = pygame.time.get_ticks()
    start_y = HEIGHT
    while True:
        screen.blit(background, (0, 0))  # Dibujar fondo del menú de opciones

        elapsed_time = pygame.time.get_ticks() - start_time
        progress = min(elapsed_time / duration, 1)
        current_y = start_y + (target_y - start_y) * progress

        # Dibujar el contenido del menú en la posición animada
        yield current_y

        if progress >= 1:
            break


def draw_volume_slider(x, y, width, height, volume, hover=False):
    slider_rect = pygame.Rect(x, y, width, height)
    slider_color = SLIDER_HOVER_COLOR if hover else SLIDER_COLOR
    pygame.draw.rect(screen, slider_color, slider_rect)
    
    # Dibuja el relleno del slider de acuerdo con el volumen
    fill_width = width * volume
    fill_rect = pygame.Rect(x, y, fill_width, height)
    pygame.draw.rect(screen, SLIDER_FILL_COLOR, fill_rect)



#def draw_studio_screen():
    #screen.blit(studio_background, (0, 0))  # Dibujar fondo de la pantalla del estudio
    #studio_text = info_font.render("Desarrollado por: Tu Estudio", True, TEXT_COLOR)
    #studio_rect = studio_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    #screen.blit(studio_text, studio_rect)
    
    # Ejemplo de información adicional, puedes ajustar o añadir más
    #credits_text = info_font.render("Versión 1.0 - 2024", True, TEXT_COLOR)
    #credits_rect = credits_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    #screen.blit(credits_text, credits_rect)

def main_menu():
    running = True
    prev_hover_button = None  # Variable para controlar si el mouse ya está sobre un botón
    
    # Pantalla del estudio (Descomentar si quieres mostrar esta pantalla)
    #draw_studio_screen()
    pygame.display.flip()
    #pygame.time.wait(3000)  # Esperar 3 segundos en la pantalla del estudio
    
    pygame.mixer.music.play(-1)  # Reproducir la música en bucle (-1 significa que se repetirá infinitamente)
    
    while running:
        screen.blit(background, (0, 0))  # Dibujar fondo del menú principal

        # Posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Dibujar el título
        draw_title("NOVELA VISUAL", WIDTH // 2, 100)  # Comenta esta línea si quieres usar una imagen de título

        # Botones
        buttons = [
            {"text": "Iniciar Juego", "x": 300, "y": 200, "width": 200, "height": 50},
            {"text": "Cargar Juego", "x": 300, "y": 270, "width": 200, "height": 50},
            {"text": "Opciones", "x": 300, "y": 340, "width": 200, "height": 50},
            {"text": "Salir", "x": 300, "y": 410, "width": 200, "height": 50},
        ]

        # Dibujar los botones y detectar si el mouse está sobre ellos
        for i, button in enumerate(buttons):
            hover = button["x"] < mouse_x < button["x"] + button["width"] and button["y"] < mouse_y < button["y"] + button["height"]
            
            # Si el mouse está sobre el botón y antes no lo estaba, reproducir sonido
            if hover and prev_hover_button != i:
                hover_sound.play()
                prev_hover_button = i  # Actualizar el botón en el que está el mouse
            elif not hover and prev_hover_button == i:
                prev_hover_button = None  # El mouse ya no está sobre el botón

            draw_rounded_button(button["text"], button["x"], button["y"], button["width"], button["height"], hover)

        # Evento de clic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]["x"] < mouse_x < buttons[0]["x"] + buttons[0]["width"] and buttons[0]["y"] < mouse_y < buttons[0]["y"] + buttons[0]["height"]:
                    print("Iniciar Juego")  # Aquí cargarías la función para iniciar el juego
                if buttons[1]["x"] < mouse_x < buttons[1]["x"] + buttons[1]["width"] and buttons[1]["y"] < mouse_y < buttons[1]["y"] + buttons[1]["height"]:
                    print("Cargar Juego")  # Función para cargar juego
                if buttons[2]["x"] < mouse_x < buttons[2]["x"] + buttons[2]["width"] and buttons[2]["y"] < mouse_y < buttons[2]["y"] + buttons[2]["height"]:
                    options_menu()  # Llamar al menú de opciones
                if buttons[3]["x"] < mouse_x < buttons[3]["x"] + buttons[3]["width"] and buttons[3]["y"] < mouse_y < buttons[3]["y"] + buttons[3]["height"]:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def options_menu():
    running = True
    prev_hover_button = None  # Variable para controlar si el mouse ya está sobre un botón

    pygame.mixer.music.play(-1)  # Reproducir la música en bucle

    # Animación de entrada
    for current_y in animate_transition(0, 500):
        screen.blit(background, (0, 0))  # Dibujar fondo del menú de opciones
        draw_title("Opciones", WIDTH // 2, 100)

        # Botones
        buttons = [
            {"text": "Volumen", "x": 300, "y": 200, "width": 200, "height": 50},
            {"text": "Controles", "x": 300, "y": 270, "width": 200, "height": 50},
            {"text": "Volver", "x": 300, "y": 340, "width": 200, "height": 50},
        ]

        # Dibujar los botones en la posición animada
        for i, button in enumerate(buttons):
            hover = button["x"] < pygame.mouse.get_pos()[0] < button["x"] + button["width"] and button["y"] < pygame.mouse.get_pos()[1] < button["y"] + button["height"]
            
            # Si el mouse está sobre el botón y antes no lo estaba, reproducir sonido
            if hover and prev_hover_button != i:
                hover_sound.play()
                prev_hover_button = i  # Actualizar el botón en el que está el mouse
            elif not hover and prev_hover_button == i:
                prev_hover_button = None  # El mouse ya no está sobre el botón

            draw_rounded_button(button["text"], button["x"], button["y"] + current_y, button["width"], button["height"], hover)

        pygame.display.flip()

    # Ciclo del menú de opciones
    while running:
        screen.blit(background, (0, 0))  # Dibujar fondo del menú de opciones

        # Posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Dibujar el título
        draw_title("Opciones", WIDTH // 2, 100)

        # Botones
        buttons = [
            {"text": "Volumen", "x": 300, "y": 200, "width": 200, "height": 50},
            {"text": "Controles", "x": 300, "y": 270, "width": 200, "height": 50},
            {"text": "Volver", "x": 300, "y": 340, "width": 200, "height": 50},
        ]

        # Dibujar los botones y detectar si el mouse está sobre ellos
        for i, button in enumerate(buttons):
            hover = button["x"] < mouse_x < button["x"] + button["width"] and button["y"] < mouse_y < button["y"] + button["height"]
            
            # Si el mouse está sobre el botón y antes no lo estaba, reproducir sonido
            if hover and prev_hover_button != i:
                hover_sound.play()
                prev_hover_button = i  # Actualizar el botón en el que está el mouse
            elif not hover and prev_hover_button == i:
                prev_hover_button = None  # El mouse ya no está sobre el botón

            draw_rounded_button(button["text"], button["x"], button["y"], button["width"], button["height"], hover)

        # Evento de clic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]["x"] < mouse_x < buttons[0]["x"] + buttons[0]["width"] and buttons[0]["y"] < mouse_y < buttons[0]["y"] + buttons[0]["height"]:
                    volume_settings_menu()  # Ir al menú de configuración de volumen
                if buttons[1]["x"] < mouse_x < buttons[1]["x"] + buttons[1]["width"] and buttons[1]["y"] < mouse_y < buttons[1]["y"] + buttons[1]["height"]:
                    # Aquí podrías abrir un submenú para los controles
                    pass
                if buttons[2]["x"] < mouse_x < buttons[2]["x"] + buttons[2]["width"] and buttons[2]["y"] < mouse_y < buttons[2]["y"] + buttons[2]["height"]:
                    return  # Regresar al menú principal

        pygame.display.flip()


def volume_settings_menu():
    running = True
    prev_hover_button = None  # Variable para controlar si el mouse ya está sobre un botón
    volume = pygame.mixer.music.get_volume()  # Obtener el volumen actual

    while running:
        screen.blit(background, (0, 0))  # Dibujar fondo del menú de opciones

        # Posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Dibujar el título
        draw_title("Configuración de Volumen", WIDTH // 2, 100)

        # Botones
        buttons = [
            {"text": "Volver", "x": 300, "y": 270, "width": 200, "height": 50},
        ]

        # Dibujar los botones y detectar si el mouse está sobre ellos
        for i, button in enumerate(buttons):
            hover = button["x"] < mouse_x < button["x"] + button["width"] and button["y"] < mouse_y < button["y"] + button["height"]
            
            # Si el mouse está sobre el botón y antes no lo estaba, reproducir sonido
            if hover and prev_hover_button != i:
                hover_sound.play()
                prev_hover_button = i  # Actualizar el botón en el que está el mouse
            elif not hover and prev_hover_button == i:
                prev_hover_button = None  # El mouse ya no está sobre el botón

            draw_rounded_button(button["text"], button["x"], button["y"], button["width"], button["height"], hover)

        # Dibujar el slider de volumen
        volume_slider_x = 300
        volume_slider_y = 200
        volume_slider_width = 200
        volume_slider_height = 20
        volume_slider_hover = (volume_slider_x < mouse_x < volume_slider_x + volume_slider_width and volume_slider_y < mouse_y < volume_slider_y + volume_slider_height)
        
        draw_volume_slider(volume_slider_x, volume_slider_y, volume_slider_width, volume_slider_height, volume, volume_slider_hover)

        # Evento de clic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]["x"] < mouse_x < buttons[0]["x"] + buttons[0]["width"] and buttons[0]["y"] < mouse_y < buttons[0]["y"] + buttons[0]["height"]:
                    return  # Regresar al menú de opciones

                # Ajuste de volumen si el slider es arrastrado
                if volume_slider_x < mouse_x < volume_slider_x + volume_slider_width and volume_slider_y < mouse_y < volume_slider_y + volume_slider_height:
                    volume = (mouse_x - volume_slider_x) / volume_slider_width
                    pygame.mixer.music.set_volume(volume)

        pygame.display.flip()

# Iniciar menú principal
main_menu()
