import pygame
import random
from classes import Jogo
from config import WIDTH, HEIGTH, INIT, GAME, GAMEOVER, QUIT
from init_screen import init_screen
from game_screen import game_screen
from gameover_screen import gameover_screen


pygame.init()
pygame.mixer.init()

if __name__ == "jogo":
    space_ship = Jogo()
    space_ship.main_loop()