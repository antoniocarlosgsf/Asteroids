import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT


def game_over_screen(screen):
    #ajustando a velocidade
    clock = pygame.time.Clock()
    #carregando a tela de game over
    tela_game_over = pygame.image.load(path.join(IMG_DIR, 'Se lascou doidim.png')).convert()