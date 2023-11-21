import pygame
import random
from config import WIDTH, HEIGTH, METEOR_WIDTH, METEOR_HEIGTH, NAVE_WIDTH, NAVE_HEIGTH
from assets import SHIP_IMG, PEW_SOUND, METEOR_IMG, BULLET_IMG, EXPLOSION_ANIM

class Nave(pygame.sprite.Sprite):
    def __init__(self. groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[SHIP_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGTH - 10
        self.speedx = 0
        self.speedy = 0
        self.assets = assets

class Meteor(pygame.sprite.Sprite):


class Bullet(pygame.sprite.Sprite):
    

class Explosion(pygame.sprite.Sprite):
    
