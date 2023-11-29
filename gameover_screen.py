# Importações
import pygame
from config import *


# Função da tela de game over
def gameover_screen(entrada):
    # Som da tela inicial
    pygame.mixer.music.load('sound/gameover_sound.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = 1)
    
    # Clock
    clock = pygame.time.Clock()

    # Fontes e textos
    font = pygame.font.SysFont('arial', 40) #Alterei para 40   
    fontAgain = pygame.font.SysFont('arial', 50) #minha
    playAgainText = fontAgain.render('Pressione "s" para jogar novamente', 1, (255, 255, 255))
    scoreText = font.render('Score: ' + str(entrada), 1, (255, 255, 255))

    
    # Loop principal da tela de game over
    perdeu = True
    while perdeu:
        # Fixando o FPS
        clock.tick(50)

        # Recebendo inputs
        for event in pygame.event.get():
            # Caso feche o jogo
            if event.type == pygame.QUIT:
                estado = SAIR
                perdeu = False
            
            # Caso deseje voltar a jogar
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    estado = JOGANDO
                    perdeu = False

        # Blita o texto e o fundo preto
        win.fill(BLACK)
        win.blit(playAgainText, (width/2 -playAgainText.get_width()/2, height/2 - playAgainText.get_height()/2))
        win.blit(scoreText, (width/2, height/4))
        

        pygame.display.flip()

    return estado