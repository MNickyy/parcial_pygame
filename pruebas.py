import pygame
import pygame.mixer

pygame.init()

    # Pantalla
pantalla = pygame.display.set_mode((1250, 650))
    # Titulo
pygame.display.set_caption("Dragon Ball: GokUTN")
    # Icono
icono = pygame.image.load("imagenes\deco\logo.jpg")
pygame.display.set_icon(icono)
    # Fondos
#fondo_inicio = pygame.image.load("fondo_inicio.jpeg")
#fondo_inicio = pygame.transform.scale(fondo_inicio,(1250, 650))
fondo_juego = pygame.image.load("imagenes/fondos/fondo_juego.jpg")
fondo_juego = pygame.transform.scale(fondo_juego,(1250, 650))

    # Música 
pygame.mixer.init()
pygame.mixer.music.load("musica\Dragon-ball-Z-soundtrack-3.wav")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

    # Cargar el sprite del personaje
personaje_sprite = pygame.image.load("imagenes\jugador\Goku4.png").convert_alpha()
personaje_sprite = pygame.transform.scale(personaje_sprite, (120, 120)) # Dimensión del personaje
personaje_rect = personaje_sprite.get_rect()
personaje_rect.topleft = (100, 500)  # Posición inicial del personaje
personaje_velocidad = 5

    # Configuración de la bala
bala_velocidad = 10
balas = []  # Lista para almacenar las balas activas
bala_sprite = pygame.image.load("imagenes\deco\disparo.png").convert_alpha()
bala_sprite = pygame.transform.scale(bala_sprite, (80, 50))


    # While de quitar el juego 
clock = pygame.time.Clock() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Reproducir sonido de disparo y crear una nueva bala
                    #disparo_sonido.play()
                bala_rect = bala_sprite.get_rect()
                bala_rect.midleft = (personaje_rect.right, personaje_rect.centery)
                balas.append(bala_rect)
    print(balas)
        
        # Movimiento del personaje con restricción de colisiones en los bordes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if personaje_rect.top > 20:  # Restricción para no salir del borde superior
            personaje_rect.y -= personaje_velocidad

    if keys[pygame.K_DOWN] and personaje_rect.bottom < 630:  # Restricción para el borde inferior
        personaje_rect.y += personaje_velocidad

        # Actualización de la posición de las balas
    for bala in balas:
        bala.x += bala_velocidad

        # Remover las balas que han salido de la pantalla
    balas = [bala for bala in balas if bala.x < 1250]

        # Pega el fondo
    pantalla.fill((0, 255, 0))
    pantalla.blit(fondo_juego, (0, 0))


    pantalla.blit(personaje_sprite, personaje_rect)  # Dibujar el sprite del personaje
    for bala in balas:
        pantalla.blit(bala_sprite, bala)
        
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)  # Limitar a 30 FPS