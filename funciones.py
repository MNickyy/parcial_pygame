import pygame
import constantes

def crear_pantalla(ancho:int, alto:int):
    pantalla = pygame.display.set_mode((ancho, alto))

    return pantalla

def cargar_imagen(archivo:str):
    imagen = pygame.image.load(archivo)

    return imagen

def iniciar_musica(archivo:str):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)