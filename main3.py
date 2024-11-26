import pygame
import pygame.mixer
import constantes
import funciones
import random



pygame.init()



    # Pantalla
pantalla = funciones.crear_pantalla(constantes.ANCHO, constantes.ALTO)
    # Titulo
pygame.display.set_caption("Dragon Ball: GokUTN")
    # Icono
icono = funciones.cargar_imagen("imagenes\deco\logo.jpg")
pygame.display.set_icon(icono)
    # Fondos
#fondo_inicio = funciones.cargar_imagen("fondo_inicio.jpeg")
#fondo_inicio = pygame.transform.scale(fondo_inicio,(constantes.ANCHO, constantes.ALTO))
fondo_juego = funciones.cargar_imagen("imagenes\\fondos\\fondo_juego.jpg")
fondo_juego = pygame.transform.scale(fondo_juego,(constantes.ANCHO, constantes.ALTO))

    # Música 
funciones.iniciar_musica("musica\Dragon-ball-Z-soundtrack-3.wav")

    # Cargar el sprite del personaje
personaje_sprite = funciones.cargar_imagen("imagenes\jugador\Goku4.png").convert_alpha()
personaje_sprite = pygame.transform.scale(personaje_sprite, (120, 120)) # Dimensión del personaje
personaje_rect = personaje_sprite.get_rect()
personaje_rect.topleft = (100, 500)  # Posición inicial del personaje


#cargar sprite enemigo
enemigo_sprite = funciones.cargar_imagen("imagenes\enemigos\cell_jr_upscaled.png").convert_alpha()
enemigo_sprite = pygame.transform.scale(enemigo_sprite, (100, 100)) # Dimensión del personaje
enemigo_sprite = pygame.transform.flip(enemigo_sprite, True, False) # invierte el sprite en el eje horizontal

enemigos = []

    # Configuración de la bala
bala_velocidad = 10
balas = []  # Lista para almacenar las balas activas
bala_sprite = pygame.image.load("imagenes\deco\disparo.png").convert_alpha()
bala_sprite = pygame.transform.scale(bala_sprite, (80, 50))


    # variables
clock = pygame.time.Clock()
personaje_velocidad = 5
enemigo_velocidad = 2
tiempo_generacion_enemigos = pygame.time.get_ticks()  # Tiempo actual
intervalo_generacion_enemigo = 2000  # 2 segundos
puntaje = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Reproducir sonido de disparo y crear una nueva bala
                    #disparo_sonido.play()
                bala_rect = pygame.Rect(personaje_rect.right, personaje_rect.centery + -20, 10, 5)
                balas.append(bala_rect)
        
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
        if bala.x > 1300: # Remover las balas que salieron de la pantalla
            balas.remove(bala)

    #apararicion de enemigos por tiempo
    if pygame.time.get_ticks() - tiempo_generacion_enemigos > intervalo_generacion_enemigo:
        enemigo_rect = enemigo_sprite.get_rect()
        enemigo_rect.x = 1250
        enemigo_rect.y = random.randint(0, 500)
        enemigos.append(enemigo_rect)
        tiempo_generacion_enemigos = pygame.time.get_ticks()

    
    #movimiento personaje
    for enemigo in enemigos:
        enemigo.x -= enemigo_velocidad
        if enemigo.x < -120:  # Eliminar enemigos que salen de pantalla
            enemigos.remove(enemigo)

    for enemigo in enemigos:
        for bala in balas:
            if bala.colliderect(enemigo): #detecta colision con de bala con enemigo y elimina los dos
                enemigos.remove(enemigo)
                balas.remove(bala)
                puntaje += 50
                print(puntaje)

    

        # Pega el fondo
    pantalla.fill((0, 255, 0))
    pantalla.blit(fondo_juego, (0, 0))


    pantalla.blit(personaje_sprite, personaje_rect)  # Dibujar el sprite del personaje
    for bala in balas:
        pantalla.blit(bala_sprite, bala)  # cargar sprite de la bala
    for enemigo in enemigos:
        pantalla.blit(enemigo_sprite, enemigo)  # cargar sprite de la enemigo
        
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS 
