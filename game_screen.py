import pygame
import math
from config import *
from funcoes import redrawGameWindow
from sprites import *
import random


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock() 


def loop_jogo():
    pygame.mixer.music.load('sound/game_sound.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    out = []
    gameover = False
    lives = 3
    score = 0
    rapidFire = False
    rfStart = -1
    
    #Inicializando jogador e lista de balas
    player = Player()
    playerBullets= []
    asteroids = []
    count = 0
    stars = [Star()]
    run = True
    while run:
        clock.tick(50)
        count += 1
        if not gameover:
            if count % 40 == 0:
                ran = random.choice([1, 1, 1, 2, 2, 3])
                asteroids.append(Asteroid(ran))
            
            if count % 2000 == 0:
                stars.append(Star())

            player.updateLocation()
            for b in playerBullets:
                b.move()
                if b.checkoffScreen():
                    playerBullets.pop(playerBullets.index(b))
            
            for a in asteroids:
                a.x += a.xv
                a.y += a.yv

                if (player.x >= a.x and player.x <= a.x + a.width) or player.x + player.width >= a.x and player.x + player.width <= a.x +a.width:
                    if (player.y >= a.y and player.y <= a.y + a.height) or player.y + player.height >= a.y and player.y + player.height <= a.y + a.height:
                        lives -= 1
                        asteroids.pop(asteroids.index(a))
                        explosion_sound.play()
                        player = Player()
                        break
                
                for b in playerBullets:
                    if (b.x >= a.x and b.x <= a.x + a.width) or b.x + b.width >= a.x and b.x + b.width <= a.x +a.width:
                        if (b.y >= a.y and b.y <= a.y + a.height) or b.y + b.height >= a.y and b.y + b.height <= a.y + a.height:
                            if a.rank == 3:
                                score += 10
                                na1 = Asteroid(2)
                                na2 = Asteroid(2)
                                na1.x = a.x
                                na2.x = a.x
                                na1.y = a.y
                                na2.y = a.y
                                asteroids.append(na1)
                                asteroids.append(na2)
                                meteor_boom.play()

                            elif a.rank == 2:
                                score += 20
                                na1 = Asteroid(1)
                                na2 = Asteroid(1)
                                na1.x = a.x
                                na2.x = a.x
                                na1.y = a.y
                                na2.y = a.y
                                asteroids.append(na1)
                                asteroids.append(na2)
                                meteor_boom.play()
                            else:
                                score += 30
                                meteor_boom.play()
                            asteroids.pop(asteroids.index(a))
                            playerBullets.pop(playerBullets.index(b))
                            #meteor_boom.play
                            
                            break

            for s in stars:
                s.x += s.xv
                s.y += s.yv
                if s.x < -100 - s.width or s.x > width + 100 or s.y > height + 100 or s.y < -100 - s.height:
                    stars.pop(stars.index(s))
                    break
                for b in playerBullets:
                    if (b.x >= s.x and b.x <= s.x + s.width) or b.x + b.width >= s.x and b.x + b.width <= s.x +s.width:
                        if (b.y >= s.y and b.y <= s.y + s.height) or b.y + b.height >= s.y and b.y + b.height <= s.y + s.height:
                            rapidFire = True
                            rfStart = count
                            stars.pop(stars.index(s))
                            playerBullets.pop(playerBullets.index(b))
                            levelup_sound.play()
                            break
            
            if lives <= 0:
                gameover = True
            if rfStart != -1:
                if count - rfStart > 500:
                    rapidFire = False
                    rfStart = -1

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.turnLeft()
            if keys[pygame.K_RIGHT]:
                player.turnRight()
            if keys[pygame.K_UP]:
                player.moveForward()
            if keys[pygame.K_SPACE]:
                if rapidFire:
                    playerBullets.append(Bullet(player))
                    pew_sound.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = SAIR
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        if not rapidFire:
                            playerBullets.append(Bullet(player))
                            pew_sound.play()

        if gameover:
            estado = FINAL
            run = False
            pontos = score
            out.append(estado)
            out.append(pontos)
                    
        redrawGameWindow(asteroids, playerBullets, stars, count, player, score, lives, gameover)

    return out