import pygame
import os
from config import METEOR_WIDTH, METEOR_HEIGTH, SHIP_WIDTH, SHIP_HEIGTH, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
METEOR_IMG ='meteor_img'
SHIP_IMG = 'ship_img'
BULLET_IMG = 'bullet_img'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'
PEW_SOUND = 'pew_sound'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background'))
    assets[METEOR_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'meteoro2' ))
    assets[METEOR_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGTH))
    assets[SHIP_IMG] = pygame.image.load(os.path.join)