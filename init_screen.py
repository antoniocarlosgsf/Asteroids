import pygame
from config import *



def init_screen():

    clock = pygame.time.Clock()

    background = pygame.image.load('imagens/AirShip.png')
    background = pygame.transform.scale(background, (width, height))
    background_rect = background.get_rect()

    running = True
    while running:

        clock.tick(50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                estado = SAIR
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    estado = JOGANDO
                    running = False
        
        win.fill(BLACK)
        win.blit(background, background_rect)

        pygame.display.flip()

    return estado