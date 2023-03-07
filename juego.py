import time
import pygame
from Bate import Bate
from Ball import Ball
import bloques


pygame.init()

# Creo la ventana del juego
WIDTH = 640
HEIGHT = 490
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ARKANOID")
fps = 60
clock = pygame.time.Clock()


# Crea el objeto bate y obtengo su rectángulo
bate = Bate(7,"imagenes/torch.png")
bate.rect.move_ip(240,450)


# Creo la pelota y le damos la velocidad y posición inicial
ball = Ball([2,2],"imagenes/ball.png")
ball.rect.move_ip(222,222)
ballrect = ball.rect.move(ball.speed)


# Creo los bloques del juego y su patrón de aparición
listaBloques = []
for pos_x in range(22):
    for pos_y in range(5):
        listaBloques.append(bloques.Block(34 * pos_x, 34 * pos_y, "imagenes/ladrillo1.png"))


# Creo el fondo del juego con una imágen
fondo = pygame.image.load("imagenes/fondo.png")
fondorect = fondo.get_rect()


# Inserto la música de fondo y la repetimos para que no se pare
musica = pygame.mixer.Sound("sonidos/minecraftmusic.mp3")
pygame.mixer.Sound.play(musica, 5)

# Muevo la pelota y compruebo si llega a los bordes de la ventana
ballrect = ball.rect.move(ball.speed)


# Inserto el bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

     # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    ballrect = ballrect.move(ball.speed)
    # Dibujo de nuevo los elementos del juego
    ventana.blit(fondo, (0, 0))
    ventana.blit(bate.imagen, bate.rect)
    # Indico que los bloques se borren de la lista y le añado un sonido
    for Block in listaBloques:
        ventana.blit(Block.image, Block.rect)
        if ballrect.colliderect(Block.rect):
            listaBloques.remove(Block)
            sonido_ladrillo = pygame.mixer.Sound("sonidos/break_sound.mp3")
            pygame.mixer.Sound.play(sonido_ladrillo)
            ball.speed[1] = -ball.speed[1]


    # Establezco los límites de los márgenes para la barra
    if keys[pygame.K_LEFT] and bate.rect.left > 0:
        bate.rect.left -= bate.speed
    if keys[pygame.K_RIGHT] and bate.rect.right < 640:
        bate.rect.right += bate.speed

    # Compruebo si hay colisión entre el bate y la pelota
    if bate.rect.colliderect(ballrect):
        ball.speed[1] = -ball.speed[1]
    ballrect = ballrect.move(ball.speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        ball.speed[0] = -ball.speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        ball.speed[1] = -ball.speed[1]
    ventana.blit(ball.imagen, ballrect)

    # Indico que los bloques se rompan con los impactos de la pelota
    if ballrect.colliderect(Block.rect):
        listaBloques.pop(Block)

    # Añado la imagen que salta cuando pierdas
    if ballrect.bottom > 480:
        youlose = pygame.image.load("imagenes/youlose.png")
        youloserect = youlose.get_rect()
        ventana.blit(youlose, (0, 0))
        sonido_youlose = pygame.mixer.Sound("sonidos/youlose.mp3")
        pygame.mixer.Sound.play(sonido_youlose)
        jugando = False


    # Añado una imágen que salta cuando ganas
    if len(listaBloques) == 0:
        youwin = pygame.image.load("imagenes/youwin.jpg")
        youwinrect = youwin.get_rect()
        ventana.blit(youwin, (0, 0))
        sonido_youwin = pygame.mixer.Sound("sonidos/youwin.mp3")
        pygame.mixer.Sound.play(sonido_youwin)
        jugando = False

    # Recargo los elementos de la pantalla y la tasa de refresco
    pygame.display.flip()
    clock.tick(fps)


# Establezco el tiempo de espera para cerrar la ventana
time.sleep(5)
pygame.quit()