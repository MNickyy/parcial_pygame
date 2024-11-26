import pygame
import pygame.mixer

pygame.init()



# Pantalla
pantalla = pygame.display.set_mode((1250, 650))
pygame.display.set_caption("Dragon Ball: GokUTN")
icono = pygame.image.load("logo.jpg")
pygame.display.set_icon(icono)
fondo_inicio = pygame.image.load("fondo_inicio.jpeg")
fondo_inicio = pygame.transform.scale(fondo_inicio,(1250, 650))
fondo_juego = pygame.image.load("fondo_juego.jpg")
fondo_juego = pygame.transform.scale(fondo_juego,(1250, 650))

# Música 
pygame.mixer.init()
pygame.mixer.music.load("Dragon-ball-Z-soundtrack-3.wav")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill((0, 255, 0))
    pantalla.blit(fondo_juego, (0, 0))
    
    pygame.display.update()