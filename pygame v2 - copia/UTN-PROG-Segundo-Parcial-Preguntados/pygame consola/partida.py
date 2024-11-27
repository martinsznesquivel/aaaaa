from ranking import *

def pedir_entero(mensaje: str, mensaje_error: str, minimo: int | bool = False, maximo: int | bool = False) -> int:
    """
    Pide un mensaje, un mensaje de error y límites opcionales mínimo y máximo.
    Muestra el mensaje y solicita que se ingrese un entero. Si el valor ingresado no está
    dentro de los límites especificados, se vuelve a pedir con el mensaje de error.

    Devuelve:
        Un número entero que cumple con los límites especificados.
    """
    retorno = int(input(mensaje))

    while (minimo != False and retorno < minimo) or (maximo != False and retorno > maximo):
        retorno = int(input(mensaje_error))

    return retorno





diccionario_preguntas = [
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["A. 1935", 
                     "B. 1939", 
                     "C. 1941", 
                     "D. 1945"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["A. Amazonas", 
                     "B. Nilo", 
                     "C. Yangtsé", 
                     "D. Misisipi"],
        "respuesta_correcta": "A"
    },
    {"pregunta": "¿Qué planeta es conocido como el 'Planeta Rojo'?",
        "opciones": ["A. Marte", 
                     "B. Júpiter", 
                     "C. Saturno", 
                     "D. Venus"],
        "respuesta_correcta": "A"
    },]


def jugar(diccionario_preguntas: dict):

    puntos = 0
    vidas_actuales = vidas_iniciales

    print("Bienvenido al preguntados")

    for i in diccionario_preguntas:
        print(f"{i["pregunta"]}  Vidas Restantes: {vidas_actuales}")
        for opcion in i["opciones"]:
            print(f"{opcion}")
        
        respuesta_usuario = input("\nTu respuesta (A, B, C o D): ").upper()
        while respuesta_usuario not in ["A", "B", "C", "D"]:
            respuesta_usuario = input ('Tu respuesta (A, B, C, D): ').upper()
        
       
        if respuesta_usuario == i["respuesta_correcta"]:
                puntos += puntos_por_respuesta
                print(f"Correcto, Puntaje actual: {puntos}")
        elif respuesta_usuario != i["respuesta_correcta"]:
            vidas_actuales -= 1
            print(f"Incorrecto, Puntaje actual: {puntos}")
            if vidas_actuales == 0:
                print("Perdiste, juego terminado")
                break
    
    print(f"Tu puntaje final es: {puntos}")
    nombre_jugador = input("Ingresa tu nombre: ")
    puntaje_final = puntos
    actualizar_ranking(nombre_jugador, puntaje_final)

def agregar_preguntas(diccionario_preguntas: list):

    pregunta_nueva = input('Ingrese la nueva pregunta: ')

    respuestas_nuevas = []
    for i in range(4):
        respuesta = input(f'Ingrese la respuesta {i+1}: ')
        respuestas_nuevas.append(respuesta)

    respuesta_correcta = input('Ingrese la opcion correcta (A, B, C, D): ').upper()

    while respuesta_correcta not in ['A', 'B', 'C', 'D']:
        print("Ingrese una opción valida")
        respuesta_correcta = input('Ingrese su respuesta (A, B, C, D): ').upper()

    nueva_pregunta = {
        "pregunta": pregunta_nueva,
        "opciones": respuestas_nuevas,
        "respuesta_correcta": respuesta_correcta
    }

    diccionario_preguntas.append(nueva_pregunta)
    print("Se agregó la pregunta")

def configurar_juego():

    puntos_por_respuesta = pedir_entero('Indique la nueva cantidad de puntos por cada respuesta correcta: ', 'Ingrese un número válido: ',)
    vidas_iniciales = pedir_entero('Indique la nueva cantidad de vidas por jugador: ', 'Ingrese un número válido: ',)

    return puntos_por_respuesta, vidas_iniciales

puntos_por_respuesta = 1
vidas_iniciales = 3


reglas_juego = False
while (True):
    opcion = pedir_entero('''Ingrese una opción.
1. Conoce las reglas del juego para comenzar
2. Empezar a jugar
3. Ver Ranking Top 10
4. Agregar preguntas
5. Configurar juego
6. Salir ''',"Error opcion invalida", 1, 6)

    
    
    match opcion:
        
        case 1:
            reglas_juego = True
            print(print('''\nEl juego consiste en una serie de preguntas las cuales tienen cuatro posibles opciones de 
respuesta, siendo una la correcta. En caso de acertar, el jugador ganará un punto y, 
caso contrario, perderá una de sus tres vidas. Si el jugador pierde todas sus vidas,
se dará por terminada la partida.\n'''))
         
        case 2:
            if reglas_juego == True:
                 jugar(diccionario_preguntas)
            else:
                print("Primero debe conocer las reglas del juego")
        case 3:
            mostrar_ranking()
        case 4:
            agregar_preguntas(diccionario_preguntas)
        case 5:
            puntos_por_respuesta, vidas_iniciales = configurar_juego()
        case 6:
           print("saliendo...")
           break