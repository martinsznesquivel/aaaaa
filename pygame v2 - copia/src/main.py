import pygame
import sys

from game.config import *

from assets.sounds import *
from assets.images import *
from prueba_ventana import *
pygame.init()

def inicializar_juego():
    '''
    Función para iniciar el juego en una ventana.

    ¿Qué hace?:
        Establece una resolución de 800x600 (ANCHO x ALTO) para el juego, un titulo y icono personalizado, el usuario puede redimensionar su tamaño usando el mouse.

        También reproduce una vez el sonido de apertura.
    '''
    ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
    pygame.display.set_caption("Preguntados [def grupo(guido, lucas, martin)]")
    pygame.display.set_icon(utn_icono)
    
    menu = pygame.image.load("assets/images icon/menu_preguntadosv1.png") #Cargo la imagen del menu
    menu = pygame.transform.scale(menu, (ANCHO, ALTO)) #Esto adapta la imagen al tamaño de ventana que nos pidieron
    
    pantalla_carga = pygame.image.load("assets/images icon/pantalla_carga.png")
    pantalla_carga = pygame.transform.scale(pantalla_carga, (ANCHO, ALTO))


    
    boton_jugar = pygame.image.load("assets/images icon/boton_jugar.png")
    boton_jugar_pos = (260, 440)

    boton_agregar = pygame.image.load("assets/images icon/boton_agregar.png")
    boton_agregar_pos = (650, 525)

    boton_configurar = pygame.image.load("assets/images icon/boton_configurar.png")
    boton_configurar_pos = (10, 525)

    boton_ver_top = pygame.image.load("assets/images icon/boton_ver_top.png")
    boton_ver_top_pos = (325, 525)

    global efecto_sonido_apertura_reproducido
    if efecto_sonido_apertura_reproducido == False:
        efecto_sonido_apertura.play()
        efecto_sonido_apertura_reproducido = True

    flag = False

    while flag== False:

        ventana.fill((0, 0, 0))
        ventana.blit(pantalla_carga,(0, 0))
        actualizar_pantalla()
        
        pygame.time.delay(int(efecto_sonido_apertura.get_length() * 1000))
        flag = True
        
    pygame.mixer.music.load("assets\sounds\music\menu_principal.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while flag == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos  # Posición del mouse al hacer clic

                # Detección de clics en los botones
                if detectar_click(boton_jugar, boton_jugar_pos, mouse_pos):
                    ventana = ventana_jugar()
                elif detectar_click(boton_agregar, boton_agregar_pos, mouse_pos):
                    ventana = ventana_agregar_preguntas()
                elif detectar_click(boton_configurar, boton_configurar_pos, mouse_pos):
                    ventana = ventana_configuracion()
                elif detectar_click(boton_ver_top, boton_ver_top_pos, mouse_pos):
                    ventana = ventana_top()


        cerrar_juego() 

        #Esto es para que se imprima la imagen del menu en la pantalla 
        ventana.fill((0, 0, 0))
        ventana.blit(menu,(0, 0))
        ventana.blit(boton_jugar,(260, 440))
        ventana.blit(boton_agregar,(650, 525))
        ventana.blit(boton_configurar,(10, 525))
        ventana.blit(boton_ver_top, (boton_ver_top_pos))
        actualizar_pantalla()

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

def crear_boton(path : str, dimensiones : tuple , posicion : tuple, funcion):
    boton = {}
    boton["surface"] = pygame.image.load(path)
    boton["surface"] = pygame.transform.scale(boton["surface"], (200, 200))
    boton["boton_pos"] = pygame.Rect((200, 200), (200, 200))
    boton["funcion"] = funcion

    return boton

def detectar_click(imagen, posicion, mouse_pos):
    '''
    Detecta si el mouse hizo clic dentro del área ocupada por una imagen.

    Args:
        imagen: Superficie (Surface) de Pygame que representa el botón.
        posicion: Tupla (x, y) con la posición superior izquierda de la imagen.
        mouse_pos: Tupla (x, y) con la posición del mouse.

    Returns:
        True si el clic ocurrió dentro del área de la imagen, False en caso contrario.
    '''
    x, y = posicion
    ancho, alto = imagen.get_size()
    return x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto

#borrar lo de arriba
inicializar_juego()
cerrar_juego()