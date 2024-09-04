# Importando o pygame
import pygame

# Iniciando o mixer 
pygame.mixer.init()

#Definindo o tamanho da tela
width = 800
height = 800


# Importando as imagens
backgroud = pygame.image.load('imagens/starbg.png')
player = pygame.image.load('imagens/player.png')
player = pygame.transform.scale(player, (50, 50))
meteorB = pygame.image.load('imagens/meteor1.png') 
meteorM = pygame.image.load('imagens/meteor2.png') 
meteorS = pygame.image.load('imagens/meteor3.png') 
star = pygame.image.load('imagens/star.png')


# Importando sons
explosion_sound = pygame.mixer.Sound('sound/explosion_sound.wav')
laser = pygame.mixer.Sound('sound/laser.wav')
meteor_boom = pygame.mixer.Sound('sound/expl3.wav')
levelup_sound = pygame.mixer.Sound('sound/levelup_sound.wav')
pew_sound = pygame.mixer.Sound('sound/laser.wav')

#Configurações da Tela
pygame.display.set_caption('AirShip') 
win = pygame.display.set_mode((width, height))

# Definindo uma variáveis para o jogo
gameover = False
lives = 3
score = 0
rapidFire = False
rfStart = -1

# Variáveis de conctrole
SAIR = 0
INICIAL = 1
JOGANDO = 2
FINAL = 3

# Cor
BLACK = (0,0,0)
WHITE = (255,255,255)
