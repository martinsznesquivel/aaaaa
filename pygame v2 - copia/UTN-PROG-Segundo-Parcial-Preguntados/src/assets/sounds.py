import pygame

pygame.init()
pygame.mixer.init()

# Efectos de sonido (assets/sounds/sfx) (.ogg, .wav)
efecto_sonido_apertura = pygame.mixer.Sound("assets/sounds/sfx/abrir_juego.wav")
efecto_sonido_apertura.set_volume(0.65)
efecto_sonido_apertura_reproducido = False

# Música (assets/sounds/music) (.mp3)