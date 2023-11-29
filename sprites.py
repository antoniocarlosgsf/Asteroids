# Importações
import pygame
import math
from config import *
import random

#Definindo a classe para o jogador
class Player():
    # Atributos
    def __init__(self):
        self.img = player
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = width/2
        self.y = height/2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)


    #Método para desenhar o jogador na tela
    def draw(self, win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    # Girando para esquerda
    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)

    # Girando para a direita  
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)
    
    # Indo para frente
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)

    # Atualizando a posição
    def updateLocation(self):
        if self.x > width + 50:
            self.x = 0
        elif self.x < 0 - self.width:
            self.x = width
        elif self.y < -50:
            self.y = height
        elif self.y > height + 50:
            self.y = 0


#Definindo a classe para a bala
class Bullet():
    # Atributos
    def __init__(self, player):
        self.point = player.head
        self.x, self.y = self.point
        self.width = 4
        self.height = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c*10
        self.yv = self.s*10
    
    
    # Movendo a bala
    def move(self):
        self.x += self.xv
        self.y -= self.yv
    
    
    # Desenhando a bala
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255),[self.x, self.y, self.width, self.height])
        
    # Verificando se a bala está fora da tela
    def checkoffScreen(self):
        if self.x + self.width < 0 or self.x > width or self.y > height or self.y + self.height< 0:
            return True 

 # Classe do asteroid       
class Asteroid():
    # Atributos
    def __init__(self, rank):
        # Diferenciando os tipos de meteoros
        self.rank = rank
        # Pequeno
        if self.rank == 1:
            self.image = meteorS
        
        # Médio
        elif self.rank == 2:
            self.image = meteorM

        # Grande  
        else:
            self.image = meteorB
                    
        self.width = 50 * rank
        self.height = 50 * rank
        # Fazendo o asteroid ser criado em um ponto aleatorio fora da tela
        self.ranPoint = random.choice([(random.randrange(0, width-self.width), random.choice([-1 * self.height - 5, height + 5])), (random.choice([-1 * self.width - 5, width + 5]), random.randrange(0, height - self.height))])
        self.x, self.y = self.ranPoint
        if self.x < width/2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < height/2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)
    
    # Desenhando
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

# Classe da estrela
class Star():
    # Atributos
    def __init__(self):
        self.img = star
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, width-self.width), random.choice([-1 * self.height - 5, height + 5])), (random.choice([-1 * self.width - 5, width + 5]), random.randrange(0, height - self.height))])  
        self.x, self.y = self.ranPoint
        if self.x < width/2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < height/2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
    
    # Desenhando
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))