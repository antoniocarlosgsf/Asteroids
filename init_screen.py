import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT

def init_screen(screen):
    #Ajuste da velocidade
    clock = pygame.time.Clock()
    
    #Carregando a tela inicial
    tela_inicial = pygame.image.load(path.join(IMG_DIR, 'tela_inicial.png')).convert()
    tela_inicial_rect = tela_inicial.get_rect()

    Statusjogo = True
    while Statusjogo:
        #ajustando a velocidade
        clock.tick(FPS)
        # Processando os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT  
                Statusjogo = False
            if event.type == pygame.KEYUP:
                state = GAME
                Statusjogo = False
        #redesenhando a tela após cada loop
        screen.fill(BLACK)
        screen.blit(tela_inicial,tela_inicial_rect)

        # invertendo o display
        pygame.display.flip()
    return state
        
            



        





