import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME

def init_screen(screen):
    #Ajuste da velocidade
    clock = pygame.time.Clock()
    
    #Carregando a tela inicial
    tela_inicial = pygame.image.load(path.join(IMG_DIR, 'tela_inicial.png')).convert()
    tela_inicial_rect = tela_inicial.get_rect()

    Statusjogo = True
    while Statusjogo:
        





