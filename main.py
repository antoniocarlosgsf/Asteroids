#Bibliotecas e funções
import pygame
from config import *
from game_screen import loop_jogo
from init_screen import init_screen
from gameover_screen import gameover_screen

pygame.mixer.init()

estado = INICIAL

#Loop principal do jogo
while estado != SAIR: 
    if estado == INICIAL:
        estado = init_screen()

    elif estado == JOGANDO:
        out = loop_jogo()
        estado = out[0]

    elif estado == FINAL:
        estado = gameover_screen(out[1])

pygame.quit()