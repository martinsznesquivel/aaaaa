import pygame 
import sys
from assets.sounds import *
from assets.images import *
import pygame
import json
import random

puntuacion = 0
puntuacion_correcta = 1
vidas = 3

def pedir_entero(mensaje: str, mensaje_error: str, minimo: int | bool = False, maximo: int | bool = False) -> int:
    """
    Pide un mensaje, un mensaje de error y límites opcionales mínimo y máximo.
    Muestra el mensaje y solicita que se ingrese un entero. Si el valor ingresado no está
    dentro de los límites especificados, se vuelve a pedir con el mensaje de error.

    Devuelve:
        Un número entero que cumple con los límites especificados.
    """

    while True:
        try:

            retorno = int(input(mensaje))

            if (minimo != False and retorno < minimo) or (maximo != False and retorno > maximo):
                print(mensaje_error)
            else:
                return retorno
        except ValueError:
            print(mensaje_error)





def configurar_juego():
    global puntuacion_correcta, vidas

    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Configuración")
    pygame.display.set_icon(utn_icono)

    ventana_configuracion = pygame.image.load("assets/images icon/fondo_agregar_pregunta.jpg") 
    ventana_configuracion = pygame.transform.scale(ventana_configuracion,(800, 600))
    ventana.blit(ventana_configuracion, (0, 0))
    
    fuente = pygame.font.Font(None, 40)
    entrada = ""
    mensaje = "Ingrese puntos por respuesta:"
    posicion = (150, 200)
    paso = 1 
    puntuacion_correcta = None
    vidas = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if paso == 1:  
                        puntuacion_correcta = int(entrada) if entrada.isdigit() else 1
                        entrada = "" 
                        mensaje = "Ingrese vidas iniciales:"
                        paso = 2
                    elif paso == 2:  
                        vidas = int(entrada) if entrada.isdigit() else 3
                        print("Configuración actualizada:", puntuacion_correcta, vidas)
                        return puntuacion_correcta, vidas
                elif event.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                elif event.unicode.isdigit():  # 
                    entrada += event.unicode

 
        ventana.blit(ventana_configuracion, (0, 0))
        texto = fuente.render(mensaje, True, (255, 255, 255))
        entrada_texto = fuente.render(entrada, True, (0, 255, 0))
        ventana.blit(texto, posicion)
        ventana.blit(entrada_texto, (posicion[0], posicion[1] + 50))

        pygame.display.flip()

def crear_boton(path: str, dimensiones: tuple, posicion: tuple, funcion):
    boton = {}
    boton["surface"] = pygame.image.load(path)
    boton["surface"] = pygame.transform.scale(boton["surface"], dimensiones)
    boton["boton_pos"] = pygame.Rect(posicion, dimensiones)  # Rectángulo en la posición correcta
    boton["funcion"] = funcion  # Almacenar la función sin ejecutarla
    return boton


def ventana_configuracion():
    pygame.init()

  
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Configuración")
    pygame.display.set_icon(utn_icono)

    ventana_configuracion = pygame.image.load("assets/images icon/fondo_agregar_pregunta.jpg") 
    ventana_configuracion = pygame.transform.scale(ventana_configuracion,(800, 600))
    ventana.blit(ventana_configuracion, (0, 0))

    
    boton_configuracion = crear_boton(
        path="assets/images icon/boton_configurar.png",
        dimensiones=(50, 50),
        posicion=(400, 300),
        funcion=lambda: configurar_juego()
    )

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_configuracion["boton_pos"].collidepoint(event.pos):
                    boton_configuracion["funcion"]()  

      
        ventana.blit(ventana_configuracion, (0, 0))
        ventana.blit(boton_configuracion["surface"], boton_configuracion["boton_pos"].topleft)
        pygame.display.flip()

    pygame.quit()

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

def inicializar_juego():
    '''
    Función para iniciar el juego en una ventana.

    ¿Qué hace?:
        Establece una resolución de 800x600 (ANCHO x ALTO) para el juego, un titulo y icono personalizado, el usuario puede redimensionar su tamaño usando el mouse.

        También reproduce una vez el sonido de apertura.
    '''
    ventana = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Preguntados [def grupo(guido, lucas, martin)]")
    pygame.display.set_icon(utn_icono)
    
    menu = pygame.image.load("assets/images icon/menu_preguntadosv1.png") #Cargo la imagen del menu
    menu = pygame.transform.scale(menu, (800, 600)) #Esto adapta la imagen al tamaño de ventana que nos pidieron
    
    pantalla_carga = pygame.image.load("assets/images icon/pantalla_carga.png")
    pantalla_carga = pygame.transform.scale(pantalla_carga, (800, 600))
    
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
                    ventana = ventana_agregar_pregunta()
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
        ventana.blit(boton_ver_top, boton_ver_top_pos)
        actualizar_pantalla()


# Función para crear un botón

def crear_boton(path: str, dimensiones: tuple, posicion: tuple, funcion):
    boton = {}
    boton["surface"] = pygame.image.load(path)
    boton["surface"] = pygame.transform.scale(boton["surface"], dimensiones)
    boton["boton_pos"] = pygame.Rect(posicion, dimensiones)  # Rectángulo en la posición correcta
    boton["funcion"] = funcion  # Almacenar la función sin ejecutarla
    return boton

# Función para volver a la ventana principal
def volver_a_ventana_principal():
   inicializar_juego()
   cerrar_juego()

def ventana_agregar_pregunta():
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Agregar Pregunta")
    pygame.display.set_icon(utn_icono)

   
    ventana_pregunta = pygame.image.load("assets/images icon/fondo_agregar_pregunta.jpg")
    ventana_pregunta = pygame.transform.scale(ventana_pregunta, (800, 600))

    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/music/menu_principal.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Crear botón
    boton_agregar_pregunta = crear_boton(
        path="assets/images icon/boton_agregar.png",  # Ruta de la imagen del botón
        dimensiones=(200, 100),               # Tamaño del botón (ancho, alto)
        posicion=(300, 300),                  # Posición del botón (x, y)
        funcion=lambda: agregar_preguntas(diccionario_preguntas)  # Función para agregar preguntas
    )

    boton_volver_inicio = crear_boton(path="assets/images icon/inicio.png", dimensiones=(50,50),posicion=(20, 20),  funcion=lambda: volver_a_ventana_principal())

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if boton_agregar_pregunta["boton_pos"].collidepoint(event.pos):
                    boton_agregar_pregunta["funcion"]()

                
                elif boton_volver_inicio["boton_pos"].collidepoint(event.pos):
                    boton_volver_inicio["funcion"]()
                    
        # Dibujar fondo y botón
        ventana.blit(ventana_pregunta, (0, 0))
        ventana.blit(boton_agregar_pregunta["surface"], boton_agregar_pregunta["boton_pos"].topleft)
        ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)
      

        pygame.display.flip()

    pygame.quit()


def agregar_preguntas(diccionario_preguntas: list):
    pregunta_nueva = input('Ingrese la nueva pregunta: ')
    respuestas_nuevas = [input(f'Ingrese la respuesta {i+1}: ') for i in range(4)]
    respuesta_correcta = input('Ingrese la opción correcta (A, B, C, D): ').upper()

    while respuesta_correcta not in ['A', 'B', 'C', 'D']:
        print("Ingrese una opción válida")
        respuesta_correcta = input('Ingrese su respuesta (A, B, C, D): ').upper()

    nueva_pregunta = {
        "pregunta": pregunta_nueva,
        "opciones": respuestas_nuevas,
        "respuesta_correcta": respuesta_correcta
    }

    diccionario_preguntas.append(nueva_pregunta)
    print("Se agregó la pregunta correctamente.")
    

diccionario_preguntas = [
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["A. 1935", "B. 1939", "C. 1941", "D. 1945"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué planeta es conocido como el 'Planeta Rojo'?",
        "opciones": ["A. Marte", "B. Júpiter", "C. Saturno", "D. Venus"],
        "respuesta_correcta": 0
    }
]


def ventana_agregar_preguntas():
    pygame.init()

    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Agregar Preguntas")

    fondo = pygame.image.load("assets/images icon/fondo_agregar_pregunta.jpg")
    fondo = pygame.transform.scale(fondo, (800, 600))

    boton_volver_inicio = crear_boton(
        path="assets/images icon/inicio.png",
        dimensiones=(50, 50),
        posicion=(20, 20),
        funcion = inicializar_juego  
    )

    boton_configuracion = crear_boton(
        path="assets/images icon/boton_configurar.png",
        dimensiones=(50, 50),
        posicion=(375, 275),  
        funcion=lambda: agregar_preguntas(diccionario_preguntas)
    )

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver_inicio["boton_pos"].collidepoint(event.pos):
                        boton_volver_inicio["funcion"]()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_configuracion["boton_pos"].collidepoint(event.pos):
                        boton_configuracion["funcion"]()  

        ventana.blit(fondo, (0, 0))
        ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)
        ventana.blit(boton_configuracion["surface"], boton_configuracion["boton_pos"].topleft)

        pygame.display.flip()

    pygame.quit()

def agregar_preguntas(diccionario_preguntas):
    entrada = ""
    mensaje = "Ingrese la pregunta:"
    paso = 1
    respuestas_nuevas = []
    respuesta_correcta = None
    pregunta_nueva = None

    ventana = pygame.display.get_surface() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    if paso == 1:
                        pregunta_nueva = entrada
                        mensaje = "Ingrese la respuesta A:"
                        entrada = ""
                        paso += 1
                    elif 2 <= paso <= 5: 
                        respuestas_nuevas.append(entrada)
                        entrada = ""
                        if paso == 5:
                            mensaje = "Ingrese la opción correcta (0, 1, 2, 3):"
                            paso += 1
                        else:
                            mensaje = f"Ingrese la respuesta {chr(65 + paso - 1)}:"
                            paso += 1
                    elif paso == 6: 
                        if entrada.isdigit() and int(entrada) in [0, 1, 2, 3]:
                            respuesta_correcta = int(entrada)  # Asigna como entero
                            nueva_pregunta = {
                                "pregunta": pregunta_nueva,
                                "opciones": respuestas_nuevas,
                                "respuesta_correcta": respuesta_correcta
                            }
                            diccionario_preguntas.append(nueva_pregunta)
                            print("Pregunta agregada:", nueva_pregunta)  
                            return  
                        else:
                            mensaje = "Opción incorrecta. Ingrese 0, 1, 2, 3"
                        entrada = ""
                elif event.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                else:
                    entrada += event.unicode

      
        ventana.fill((255, 255, 255))  

        
        fuente = pygame.font.Font(None, 36)
        texto_mensaje = fuente.render(mensaje, True, (0, 0, 0))  
        ventana.blit(texto_mensaje, (50, 50))

        texto_entrada = fuente.render(entrada, True, (0, 0, 255))  
        ventana.blit(texto_entrada, (50, 100))


        pygame.display.flip()

def ventana_jugar():

    global puntuacion_correcta, vidas
    puntuacion = 0

    pantalla_jugar = pygame.image.load("assets/images icon/fondo_jugar.png")
    pantalla_jugar = pygame.transform.scale(pantalla_jugar, (800, 600))
    
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jugar")
    pygame.display.set_icon(utn_icono)

    random.shuffle(diccionario_preguntas)

    fuente = pygame.font.Font(None, 36)

    pregunta_actual = 0
    mostrando_respuesta = False
    color_respuesta = (255, 255, 0)

    corriendo = True
    while corriendo:

        ventana.blit(pantalla_jugar, (0, 0)) 

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                corriendo = False

            if evento.type == pygame.MOUSEBUTTONDOWN and not mostrando_respuesta:
                mouse_pos = pygame.mouse.get_pos()
                for i, opcion_rect in enumerate(opciones_rects):
                    if opcion_rect.collidepoint(mouse_pos):

                        if i == diccionario_preguntas[pregunta_actual]["respuesta_correcta"]:
                            puntuacion += puntuacion_correcta
                            color_respuesta = ((0, 255, 0))
                            
                        else:
                            vidas -= 1
                            color_respuesta = ((255, 0, 0))
                        mostrando_respuesta = True
                        break

        # Mostrar pregunta
        pregunta_texto = fuente.render(
            diccionario_preguntas[pregunta_actual]["pregunta"], True, ((0, 0, 0))
        )
        ventana.blit(pregunta_texto, (50, 50))

        # Mostrar opciones
        opciones_rects = []
        for i, opcion in enumerate(diccionario_preguntas[pregunta_actual]["opciones"]):
            opcion_texto = fuente.render(opcion, True, (0, 0, 0))
            opcion_rect = opcion_texto.get_rect(topleft=(50, 150 + i * 50))
            opciones_rects.append(opcion_rect)
            ventana.blit(opcion_texto, opcion_rect.topleft)

        # Mostrar respuesta si está en modo de respuesta
        if mostrando_respuesta:
            pygame.draw.rect(
                ventana,
                color_respuesta,
                opciones_rects[diccionario_preguntas[pregunta_actual]["respuesta_correcta"]],
                3,
            )
            pygame.time.wait(2000)  # Esperar 2 segundos
            mostrando_respuesta = False
            color_respuesta = (0, 0, 0)
            pregunta_actual += 1
            if pregunta_actual >= len(diccionario_preguntas):
                corriendo = False

        # Mostrar puntuación y vidas
        puntuacion_texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        vidas_texto = fuente.render(f"Vidas: {vidas}", True, (255, 0, 0))
        ventana.blit(puntuacion_texto, (50, 500))
        ventana.blit(vidas_texto, (650, 500))

        # Revisar si se acabaron las vidas
        if vidas == 0:
            corriendo = False
        
        pygame.display.flip()

        # Pantalla final o gameover

    ventana.fill((0, 0, 0))
    mensaje_final = fuente.render("¡Fin del juego!", True, (255, 255, 255))
    puntuacion_final = fuente.render(f"Puntuación final: {puntuacion}", True, (255, 255, 255))
    ventana.blit(mensaje_final, (300, 250))
    ventana.blit(puntuacion_final, (300, 300))
    pygame.display.flip()
    pygame.time.wait(3000)

    nombre = solicitar_nombre(ventana, fuente)
    guardar_clasificacion(nombre, puntuacion)
    volver_a_ventana_principal()


def ventana_configuracion():
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Configuracion")
    pygame.display.set_icon(utn_icono)

    ventana_configuracion = pygame.image.load("assets/images icon/fondo_agregar_pregunta.jpg") 
    ventana_configuracion = pygame.transform.scale(ventana_configuracion,(800, 600))
    ventana.blit(ventana_configuracion, (0, 0))

    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/music/menu_principal.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)



    boton_volver_inicio = crear_boton(path="assets/images icon/inicio.png", dimensiones=(50,50),posicion=(20, 20),  funcion=lambda: volver_a_ventana_principal())
    boton_configuracion = crear_boton(
        path="assets/images icon/boton_configurar.png",  # Ruta de la imagen del botón
        dimensiones=(200, 100),               # Tamaño del botón (ancho, alto)
        posicion=(300, 300),                  # Posición del botón (x, y)
        funcion=lambda:configurar_juego() # Función para agregar preguntas
    )

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if boton_configuracion["boton_pos"].collidepoint(event.pos):
                    boton_configuracion["funcion"]()

                
                elif boton_volver_inicio["boton_pos"].collidepoint(event.pos):
                    boton_volver_inicio["funcion"]()
                    
        # Dibujar fondo y botón
        ventana.blit(ventana_configuracion, (0, 0))
        ventana.blit(boton_configuracion["surface"], boton_configuracion["boton_pos"].topleft)
        ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)
      

        pygame.display.flip()

def cargar_clasificacion(ruta_json):
    try:
        with open(ruta_json, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_json}")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_json} no tiene un formato JSON válido")
        return []

def solicitar_nombre(ventana, fuente):
    bandera = True
    nombre = ""
    while bandera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    bandera = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        # Mostrar entrada de texto
        ventana.fill((0, 0, 0))
        mensaje = fuente.render("Ingrese su nombre y presione Enter:", True, (255, 255, 255))
        texto_nombre = fuente.render(nombre, True, (255, 255, 255))
        ventana.blit(mensaje, (50, 250))
        ventana.blit(texto_nombre, (50, 300))
        pygame.display.flip()

    return nombre

def guardar_clasificacion(nombre, puntuacion):
    archivo = "ranking.json"
    try:

        with open(archivo, "r") as f:
            clasificacion = json.load(f)
    except FileNotFoundError:

        clasificacion = []

    clasificacion.append({"nombre": nombre, "puntuacion": puntuacion})

    clasificacion = sorted(clasificacion, key=lambda x: x["puntuacion"], reverse=True)

    # Guardar de nuevo el archivo
    with open(archivo, "w") as f:
        json.dump(clasificacion, f, indent=4)

def graficar_clasificacion(ventana, clasificacion, fuente, posicion_inicial):
    y_offset = 0
    for indice, jugador in enumerate(clasificacion):
        texto = f"{indice + 1}. {jugador['nombre']} - {jugador['puntuacion']} puntos"
        texto_render = fuente.render(texto, True, (255, 255, 255))
        ventana.blit(texto_render, (posicion_inicial[0], posicion_inicial[1] + y_offset))
        y_offset += 30

def ventana_top():

    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mostrar la tabla de clasificación")
    utn_icono = pygame.image.load("assets/images icon/boton_ver_top.png")
    pygame.display.set_icon(utn_icono)

    ventana_top = pygame.image.load("assets/images icon/fondo_ranking.jpg")
    ventana_top = pygame.transform.scale(ventana_top, (800, 600))

    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/music/menu_principal.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    fuente = pygame.font.Font(None, 36)

    ruta_json = "ranking.json"
    clasificacion = cargar_clasificacion(ruta_json)

    boton_volver_inicio = crear_boton(
        path="assets/images icon/inicio.png", 
        dimensiones=(50, 50),
        posicion=(20, 20),
        funcion=lambda: print("Volver al inicio")
    )

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        ventana.blit(ventana_top, (0, 0))
        graficar_clasificacion(ventana, clasificacion, fuente, (325, 300))
        ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)

        pygame.display.flip()
    
    pygame.quit()
