import pygame
import sys

from src.game.config import *

from src.assets.sounds import *
from src.assets.images import *


pygame.init()

def inicializar_juego():
    '''
    Función para iniciar el juego en una ventana.

    ¿Qué hace?:
        Establece una resolución de 800x600 (ANCHO x ALTO) para el juego, un titulo y icono personalizado, el usuario puede redimensionar su tamaño usando el mouse.

        También reproduce una vez el sonido de apertura.
    '''
    pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
    pygame.display.set_caption("Preguntados [def grupo(guido, lucas, martin)]")
    pygame.display.set_icon(utn_icono)
    
    global efecto_sonido_apertura_reproducido
    if efecto_sonido_apertura_reproducido == False:
        efecto_sonido_apertura.play()
        efecto_sonido_apertura_reproducido = True
    
    # prueba de música
    #pygame.time.delay(int(efecto_sonido_apertura.get_length() * 1000))
    #pygame.mixer.music.load("assets\sounds\music\menu_principal.mp3")
    #pygame.mixer.music.set_volume(0.5)
    #pygame.mixer.music.play(-1)

def cerrar_juego():
    '''
    Función que maneja el cierre de la ventana del juego.

    Esta función revisa los eventos de Pygame, si detecta que el usuario
    cierra la ventana del juego (Por ejemplo: al hacer clic en la "X"),
    se termina el juego de forma segura.

    pygame.quit(): Cierra la ventana actual del juego.
    sys.exit(): Finaliza el proceso del juego (Usado para salir del bucle principal)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def actualizar_pantalla():
    pygame.display.update()