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
        self.groups = groups

        # Só será possível atirar uma vez a cada 300 milisegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 300

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self):
        now = pygame.time.get_tickes()
        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem
            self.last_shot = now

class Meteor(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[METEOR_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get.rect()
        
    



class Bullet(pygame.sprite.Sprite):


class Explosion(pygame.sprite.Sprite):
    
