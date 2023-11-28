import pygame

#Definindo o tamanho da tela
width = 800
height = 800


#importando as imagens
backgroud = pygame.image.load('img/starbg.png')
player = pygame.image.load('img/player.png')
meteorB = pygame.image.load('img/meteor1.png') 
meteorM = pygame.image.load('img/meteor2.png') 
meteorS = pygame.image.load('img/meteor3.png') 
#bullet = pygame.image.load('img/bullet.png')  #nao foi utilizada, criei a bala com o "draw"
star = pygame.image.load('img/star.png')


#Configurações da Tela
pygame.display.set_caption('Asteroids') 
win = pygame.display.set_mode((width, height))

#Definindo uma variável para o jogo
gameover = False
lives = 3
score = 0
rapidFire = False
rfStart = -1

SAIR = 0
INICIAL = 1
JOGANDO = 2
FINAL = 3
