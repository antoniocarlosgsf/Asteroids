#Biblioteca do Jogo
import pygame
#Tamanho da Janela  
width = 800
height = 800

gameover = False
lives = 3
score = 0
rapidFire = False
rfStart = -1

#importando as imagens
backgroud = pygame.image.load('img/starbg.png')
player = pygame.image.load('img/player.png')
meteorB = pygame.image.load('img/meteor1.png') 
meteorM = pygame.image.load('img/meteor2.png') 
meteorS = pygame.image.load('img/meteor3.png') 
enemy = pygame.image.load('img/enemy.png')
star = pygame.image.load('img/star.png')


#Configurações da Tela
pygame.display.set_caption('Asteroids') 
win = pygame.display.set_mode((width, height)) 
