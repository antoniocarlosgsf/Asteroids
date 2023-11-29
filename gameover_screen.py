import pygame
from config import *


def gameover_screen(entrada):
    pygame.mixer.music.load('sound/gameover_sound.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = 1)
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('arial', 40) #Alterei para 40   
    fontAgain = pygame.font.SysFont('arial', 50) #minha
    playAgainText = fontAgain.render('Pressione "s" para jogar novamente', 1, (255, 255, 255))
    scoreText = font.render('Score: ' + str(entrada), 1, (255, 255, 255))

    

    perdeu = True
    while perdeu:

        clock.tick(50)

        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = SAIR
                perdeu = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    estado = JOGANDO
                    perdeu = False

        win.fill(BLACK)
        win.blit(playAgainText, (width/2 -playAgainText.get_width()/2, height/2 - playAgainText.get_height()/2))
        win.blit(scoreText, (width/2, height/4))
        

        pygame.display.flip()

    return estado