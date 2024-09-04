# Importações
import pygame
from config import *
from funcoes import playMusic


# Função da tela inicial
def init_screen():
    # Som de game over
    playMusic('sound/inicial_sound.wav')

    # Clock
    clock = pygame.time.Clock()

    # Importando imagem e colocando na escala
    background = pygame.image.load('imagens/AirShip.png')
    background = pygame.transform.scale(background, (width, height))
    background_rect = background.get_rect()

    # Loop principal da tela inicial
    running = True
    while running:
        # Fixando o FPS
        clock.tick(50)

        # Recebendo interação do player
        for event in pygame.event.get():
            # Se fechar o jogo
            if event.type == pygame.QUIT:
                estado = SAIR
                running = False

            # Se desejar iniciar o jogo
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    estado = JOGANDO
                    running = False
        
        # Preenche o fundo e blita a imagem
        win.fill(BLACK)
        win.blit(background, background_rect)

        pygame.display.flip()

    return estado