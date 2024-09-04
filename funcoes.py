# Importações
import pygame
from config import *


#Função para redesenhar a tela do jogo
def redrawGameWindow(asteroids, playerBullets, stars, count, player, score, lives, gameover, rapidFire):

    # Definindo janela fontes, textos, tamanhos e cores
    win.blit(backgroud, (0,0))
    font = pygame.font.SysFont('arial', 40) #Alterei para 40
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    fontAgain = pygame.font.SysFont('arial', 60) #minha
    playAgainText = fontAgain.render('Pressione Espaço para jogar novamente', 1, (255, 255, 255))
    scoreText = font.render('Score: ' + str(score), 1, (255, 255, 255))

    # Desenhando os objetos do jogo
    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    for s in stars:
        s.draw(win)
    
    # Desenha barra de tempo do poder
    if rapidFire:
        pygame.draw.rect(win, (0, 0, 0), [width/2 - 51, 19, 102, 22])
        pygame.draw.rect(win, (255, 255, 255), [width/2 - 50, 20, 100 - 100 * (count - rfStart)/500, 20])
    
    
    # Blitando a vida e a pontuação
    win.blit(scoreText, (width - scoreText.get_width() - 25, 25))
    win.blit(livesText, (25, 25))
    pygame.display.update()

def playMusic(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = 1)