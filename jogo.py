import pygame
import random
from config import WIDTH, HEIDTH, INIT, GAME, GAMEOVER, QUIT
from init_screen import init_screen
from game_screen import game_screen


pygame.init()
pygame.mixer.init()

# -- Gerando tela inicial -- #
window = pygame.display.set_mode((WIDTH, HEIDTH))
pygame.display.set_caption('Asteroids')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == GAMEOVER:
        state = gameover_screen(window)
    else:
        state = QUIT

# -- Finalizando o jogo -- #
pygame.quit()