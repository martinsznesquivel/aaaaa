from main import *

class PantallaSecundaria:

    def cambiar_pantalla_juego(self):
        print("hola")
    def cambiar_pantalla_agregar(self):
        print('hola')

    def cambiar_pantalla_configurar(self):
        print('hola')

lista_botones = []

def __init__(self):

    if len(self.lista_botones) == 0:
        boton_jugar = crear_boton("assets/images icon/boton_jugar.png", (275, 70), (260, 440), self.cambiar_pantalla_juego)
        boton_agregar = crear_boton("assets/images icon/boton_agregar.png", (140, 64), (650, 525), self.cambiar_pantalla_agregar)
        boton_configurar = crear_boton("assets/images icon/boton_configurar.png", (140, 64), (10, 525), self.cambiar_pantalla_configurar)

        self.lista_botones.append(boton_jugar)
        self.lista_botones.append(boton_agregar)
        self.lista_botones.append(boton_configurar)

    if self.flag_click:
        for boton in self.lista_botones:
            if boton['boton_pos'].collidepoint(self.mouse_pos):
                boton['funcion']()