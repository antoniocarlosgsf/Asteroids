from os import path

# Estabelece a pasta que contem as figuras e sons
IMG_DIR = path.join(path.dirname(__file__), 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'sound')
FNT_DIR = path.join(path.dirname(__file__), 'Font')

# Dados gerais do jogo
WIDTH = 900
HEIDTH = 900
FPS = 30

METEOR_WIDTH = 50
METEOR_HEIGTH = 38
SHIP_WIDTH = 40
SHIP_HEIGTH = 31


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

INIT = 0
GAME = 1
GAMEOVER = 2
QUIT = 3
