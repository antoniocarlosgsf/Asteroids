import pygame

#Definindo o tamanho da tela
width = 800
height = 800


#importando as imagens
backgroud = pygame.image.load('imagens/starbg.png')
player = pygame.image.load('imagens/player.png')
meteorB = pygame.image.load('imagens/meteor1.png') 
meteorM = pygame.image.load('imagens/meteor2.png') 
meteorS = pygame.image.load('imagens/meteor3.png') 
star = pygame.image.load('imagens/star.png')


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

BLACK = (0,0,0)
