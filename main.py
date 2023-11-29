#Bibliotecas e funções
import pygame
from config import *
from game_screen import loop_jogo
from init_screen import init_screen
from gameover_screen import gameover_screen

# Inicia o mixer
pygame.mixer.init()

estado = INICIAL

#Loop principal do jogo
while estado != SAIR: 
    # Tela inicial
    if estado == INICIAL:
        estado = init_screen()

    # Tela do jogo
    elif estado == JOGANDO:
        out = loop_jogo()
        estado = out[0]

    # Tela de game over
    elif estado == FINAL:
        estado = gameover_screen(out[1])

# Finaliza o jogo
pygame.quit()