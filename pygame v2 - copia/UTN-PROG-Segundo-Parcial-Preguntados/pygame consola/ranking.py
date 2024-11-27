import json
import os

archivo_ranking = "ranking.json"

def cargar_ranking():
    """Carga el ranking desde el archivo JSON o crea uno vacío si no existe."""
    if os.path.exists(archivo_ranking):
        with open(archivo_ranking, "r") as archivo:
            return json.load(archivo)
    return []  

def guardar_ranking(ranking):
    
    with open(archivo_ranking, "w") as archivo:
        json.dump(ranking, archivo, indent=4)

def actualizar_ranking(nombre, puntaje):
    """Actualiza el ranking con el nuevo puntaje."""
  
    ranking = cargar_ranking()
    
   
    ranking.append({"nombre": nombre, "puntaje": puntaje})

    #ranking.sort()
    
    
    
  
    ranking = ranking[:10]
   
    guardar_ranking(ranking)

def mostrar_ranking():
    """Muestra el ranking en pantalla."""
    ranking = cargar_ranking()
    print("\n--- TOP 10 Ranking ---")
    for i, jugador in enumerate(ranking, start=1):
        print(f"{i}. {jugador['nombre']} - {jugador['puntaje']}")
    print("----------------------")

