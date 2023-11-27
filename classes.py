import pygame
import math
from config import *
import random

class Player(object):
    def __init__(self):
        self.img = player
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = width/2
        self.y = height/2
        
        
        
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)


    #Método para desenhar o jogador na tela
    def draw(self, win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)

        
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width/2, self.y - self.sine * self.height/2)
    # há a possibilidade de criar uma seta para trás 
    
    def updateLocation(self):
        if self.x > width + 50:
            self.x = 0
        elif self.x < 0 - self.width:
            self.x = width
        elif self.y < -50:
            self.y = height
        elif self.y > height + 50:
            self.y = 0


#Definindo a classe para a bala
class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.width = 4
        self.height = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c*10
        self.yv = self.s*10
    
    
    #Método para mover a bala
    def move(self):
        self.x += self.xv
        self.y -= self.yv
    
    
    #Método para desenhar a bala
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255),[self.x, self.y, self.width, self.height])
            #importante, não utilizo imagem da bala e sim o desenho dela
    
    
    #Método para verificar se a bala está fora da tela
    def checkoffScreen(self):
        if self.x + self.width < 0 or self.x > width or self.y > height or self.y + self.height< 0:
            return True 
        
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = meteorS
        
        elif self.rank == 2:
            self.image = meteorM
            
        else:
            self.image = meteorB
                    
        self.width = 50 * rank
        self.height = 50 * rank
        #Esta linha cria um ponto de posição inicial aleatória para o asteroide, garantindo que ele comece fora da tela em uma das bordas.
        self.ranPoint = random.choice([(random.randrange(0, width-self.width), random.choice([-1 * self.height - 5, height + 5])), (random.choice([-1 * self.width - 5, width + 5]), random.randrange(0, height - self.height))])
        self.x, self.y = self.ranPoint
        if self.x < width/2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < height/2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
class Star(object):
    def __init__(self):
        self.img = star
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, width-self.width), random.choice([-1 * self.height - 5, height + 5])), (random.choice([-1 * self.width - 5, width + 5]), random.randrange(0, height - self.height))])  
        self.x, self.y = self.ranPoint
        if self.x < width/2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < height/2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
    
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

#Função para redesenhar a tela do jogo
def redrawGameWindow():
    win.blit(backgroud, (0,0))
    font = pygame.font.SysFont('arial', 40) #Alterei para 40
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    fontAgain = pygame.font.SysFont('arial', 60) #minha
    playAgainText = fontAgain.render('Press Space to Play Again', 1, (255, 255, 255))
    scoreText = font.render('Score: ' + str(score), 1, (255, 255, 255))


    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    for s in stars:
        s.draw(win)
    
    if rapidFire:
        pygame.draw.rect(win, (0, 0, 0), [width/2 - 51, 19, 102, 22])
        pygame.draw.rect(win, (255, 255, 255), [width/2 - 50, 20, 100 - 100 * (count - rfStart)/500, 20])
    
    
    if gameover:
        win.blit(playAgainText, (width/2 -playAgainText.get_width()/2, height/2 - playAgainText.get_height()/2))
    win.blit(scoreText, (width - scoreText.get_width() - 25, 25))
    win.blit(livesText, (25, 25))
    pygame.display.update()


#Inicializando jogador e lista de balas
player = Player()
playerBullets= []
asteroids = []
count = 0
stars = [Star()]
#Loop principal do jogo
run = True
while run:
    clock.tick(50)
    count += 1
    if not gameover:
        if count % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(ran))
        
        if count % 1000 == 0:
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
                        else:
                            score += 30
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
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
                playerBullets.append(Bullet())


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    if not rapidFire:
                        playerBullets.append(Bullet())
                else:
                    gameover = False
                    lives = 3
                    score = 0
                    asteroids.clear()

    
    redrawGameWindow()