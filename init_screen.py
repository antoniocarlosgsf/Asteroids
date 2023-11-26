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
    #Carregando a tela de game over
    tela_game_over = pygame.image.load(path.join(IMG_DIR, 'Se lascou doidim(1).png')).convert()
    tela_game_over_rect = tela_game_over.get_rect()

    Statusjogo = "inicio do jogo"

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYUP:
                if Statusjogo == "inicio do jogo":
                    Statusjogo == "game"
                elif Statusjogo == "game":
                    Statusjogo == "game_over"
                #vou adicionar ainda  a lógica para quando morre
                elif Statusjogo == "game_over":
                    if event.key == pygame.K_BACKSPACE:
                        #tem que adicionar aqui a lógica para reiniciar
                        Statusjogo ="game"
                        reiniciar()#tem que botar a função de reinicio
        
        screen.fill(BLACK)

        if Statusjogo == "inicio do jogo":
            screen.blit((tela_inicial,tela_inicial_rect))
        elif Statusjogo == "game":
            pass
        elif Statusjogo == "game_over":
            screen.blit(tela_game_over,tela_game_over_rect)
        
        pygame.display.flip()

                    