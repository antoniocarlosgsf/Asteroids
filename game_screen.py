import pygame
from config import FPS, WIDTH, HEIDTH, BLACK, YELLOW, RED
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, SCORE_FONT
from sprites import Nave, Meteor, Bullet, Explosion

def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_bullets'] = all_bullets

    # Criando o jogador
    player = Nave(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    
