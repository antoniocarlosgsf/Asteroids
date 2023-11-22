import pygame
import random
from funcoes import load_sprite
from config import WIDTH, HEIGTH, METEOR_WIDTH, METEOR_HEIGTH, NAVE_WIDTH, NAVE_HEIGTH, BLACK, FPS
from assets import SHIP_IMG, PEW_SOUND, METEOR_IMG, BULLET_IMG, EXPLOSION_ANIM
from pygame.math import Vector2
from pygame.transform import rotozoom

UP = Vector2(0, -1)

class Jogo:
    def __init__(self):
        self.init_pygame()
        self.tela = pygame.display.set_mode((WIDTH, HEIGTH))
        self.background = pygame.transform.scale(load_sprite("background", False), (WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.meteoro = Objetos((METEOR_WIDTH, METEOR_HEIGTH), load_sprite('meteoro1'), (1, 0))
        self.nave = Nave((NAVE_WIDTH, NAVE_HEIGTH))

    def main_loop(self):
        while True:
            self.event()
            self.logica_jogo()
            self.draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption(" SPACE SHIP")

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        pressionada = pygame.key.get_pressed()

        if pressionada[pygame.K_RIGHT]:
            self.nave.rotate(horario=True)
        elif pressionada[pygame.K_LEFT]:
            self.nave.rotate(horario=False)

    def logica_jogo(self):
        self.nave.updade()
        self.meteoro.updade()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.nave.draw(self.tela)
        self.meteoro.draw(self.tela)
        pygame.display.flip()
        self.clock.tick(FPS)

class Objetos:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def updade(self):
        self.position += self.velocity

    def colisao(self, other_obj):
        distance = self.position.distance_to(outro_obj.position)
        return distance < self.radius + outro_obj.radius    

class Nave(Objetos):
    def __init__(self, posicao):
        self.direcao = Vector2(UP)
        super().__init__(posicao, load_sprite('Nave'), Vector2(0))
    ROTACAO = 3

    def rotate(self, horario=True):
        sign = 1 if horario else -1
        angulo = self.ROTACAO*sign
        self.direction.rotate_ip(angulo)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotacionada = rotozoom(self.sprite, angle, 1.0)
        tamanho_rotacionada = Vector2(rotacionada.get_size())
        blit_position = self.position - tamanho_rotacionada*0.5
        surface.blit(rotacionada, blit_position)

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
        self.rect.x = random.randint(-METEOR_WIDTH, WIDTH+METEOR_WIDTH)
        self.rect.y = random.randint(-100, HEIGTH+METEOR_HEIGTH)
        while (self.rect.x >= 0 and self.rect.x <= WIDTH - METEOR_WIDTH) and (self.rect.y >= -METEOR_HEIGTH and self.rect.y <= HEIGTH + METEOR_HEIGTH):
            self.rect.x = random.randint(-METEOR_WIDTH, WIDTH+METEOR_WIDTH)
            self.rect.y = random.randint(-100, HEIGTH+METEOR_HEIGTH)
        self.speedx = random.randint(-3, 3)
        self.speedy = random. randint(2,9)

    def update(self):
        # Atualiza a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro sair da tela, é resorteada sua posição
        if self.rect.top > HEIGTH or self.rect.rigth 
        
        
    



class Bullet(pygame.sprite.Sprite):
    

class Explosion(pygame.sprite.Sprite):
    
