import pygame
import os
from config import METEOR_WIDTH, METEOR_HEIGTH, SHIP_WIDTH, SHIP_HEIGTH, IMG_DIR, SND_DIR, FNT_DIR, 


BACKGROUND = 'background'
METEOR_IMG ='meteor_img'
SHIP_IMG = 'ship_img'
BULLET_IMG = 'bullet_img'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'
PEW_SOUND = 'pew_sound'
INIT_IMG = ''

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.avif')).convert()
    assets[METEOR_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'meteoro2.png' )).convert_alpha()#acrescentei ''.convert_alpha''
    assets[METEOR_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGTH))
    assets[SHIP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Nave.png')).convert_alpha()#acrescentei ''.convert_alpha''
    assets[SHIP_IMG]= pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGTH))
    #pensando sobre colocar uma sequencia de explosões ou a mudança do tamanho do meteoro
    assets[BULLET_IMG]= pygame.image.load(os.path.join(IMG_DIR, 'tiro.jpg')).convert_alpha()
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
