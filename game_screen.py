import pygame
from config import FPS, WIDTH, HEIDTH, BLACK, YELLOW, RED
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, SCORE_FONT
from sprites import Nave, Meteor, Bullet, Explosion

def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_bullets'] = all_bullets

    # Criando o jogador
    player = Nave(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    for i in range(8):
        meteor = Meteor(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

    # Loop principal
    while state != DONE:
        clock.tick(FPS)

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.speedx = -4
                if event.key == pygame.K_RIGHT:
                    player.speedx += 4
                if event.key == pygame.K_UP:
                    player.speedy -= 4
                if event.key == pygame.K_DOWN:
                    player.speedy += 4
                if event.key == pygame.K_SPACE:
                    player.shoot()
            # Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 4
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 4
                    if event.key == pygame.K_UP:
                        player.speedy += 4
                    if event.key == pygame.K_DOWN:
                        player.speedy -= 4
        # Atualiza estado do jogo
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
            for meteor in hits:
                assets[DESTROY_SOUND].play()
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)

                # Adicionar uma explosão
                explosao = Explosion(meteor.rect.center, assets)
                all_sprites.add(explosao)

                # Ganhou pontos!
                score += 100
                if score % 1000 == 0:
                    lives += 1

            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state == PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

        # Gerando saídas
        window.fill(BLACK)
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteóros
        all_sprites.draw(window)

        pygame.display.update()

