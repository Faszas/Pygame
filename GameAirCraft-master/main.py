'''
    @Author: Faszas  Modified: 9.11.2019
    @Content : Game AirCraft
    @Music : 135_Alan_Walker
'''
import pygame
import random
import math

from pygame import mixer
# initialize pygame
pygame.init()

# create the screen ( tao man hinh de choi game )
screen = pygame.display.set_mode((800,600))

# TItle and icon
    # Change title ^^
pygame.display.set_caption(" Aircraft ")
    #change incon
incon = pygame.image.load("images.png")
pygame.display.set_icon(incon)

# Background
background = pygame.image.load("andromeda_galaxy-800x600.png")
# background music
mixer.music.load("135 - Alan Walker (NhacPro.net).mp3")
mixer.music.play(-1)
#player
class PLAYER(object):
    def __init__(self, playerX, playerY, playerX_change ):
        self.playerImg = pygame.image.load("war.png")
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
    def showPlayer(self, x, y):
        screen.blit(self.playerImg, (x, y))
 # playerX = 370  playerY = 480 playerX_change = 0
#enemy
class ENEMY(object):
    def __init__(self):
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.numberEnemy = 6
    def CreateEnemy(self):
        for i in range(self.numberEnemy):
            self.enemyImg.append(pygame.image.load("spooky.png"))
            self.enemyX.append(random.randint(0, 735))
            self.enemyY.append(random.randint(0, 150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)
    def showEnemy(self, x, y, i):
        screen.blit(self.enemyImg[i], (x, y))
# bullet
# ready = you can't see the bullet on the screen
# fire - the bullet is currently moving
class BULLET(object):
    def __init__(self, bulletX, bulletY, bulletX_change, bulletY_change):
        self.bulletImg = pygame.image.load("bullet.png")
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletX_change = bulletX_change
        self.bulletY_change = bulletY_change
        self.bullet_state = "ready"
    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        screen.blit(self.bulletImg, (x + 24, y - 20))
#score
class SCORE(object):
    def __init__(self, score_value, textX, textY, temp):
        self.score_value = score_value
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.textX = textX
        self.textY = textY
        self.temp = temp
    def show_score(self, x, y):
        self.score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(self.score, (x, y))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = (math.sqrt(math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance <= 35:
        return True
    else:
        return False
# game over text
over_font = pygame.font.Font("freesansbold.ttf",70)

def game_over_text():
    over_text = font.render("GAME OVER",True,(255,0,0))
    screen.blit(over_text, (200,250))
def BACKGROUND():
    # RGB = red , green , blue
    screen.fill((10, 0, 0))
    # background image
    screen.blit(background, (0, 0))
# Main Loop
man = PLAYER(370, 480, 0)
Monster = ENEMY()
Monster.CreateEnemy()
bullet = BULLET(0, 480, 0, 10)
score = SCORE(0, 10, 10, 0)
running = True
while running:
    BACKGROUND()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            man.playerX_change = -5
        if event.key == pygame.K_RIGHT:
            man.playerX_change = 5
        if event.key == pygame.K_SPACE:
            if bullet.bullet_state == "ready":
                # Get the current x cordinate of the aircraft
                bullet.bulletX = man.playerX
                bullet.fire_bullet(bullet.bulletX, bullet.bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            man.playerX_change  = 0
    # checking boundaries of aircraft so it doesn't go out bounds
    man.playerX += man.playerX_change

    if man.playerX <= 0:
        man.playerX = 0
    elif man.playerX >= 736:
        man.playerX = 736

    # enemy movement
    for i in range(Monster.numberEnemy):
        Monster.enemyX[i] += Monster.enemyX_change[i]
        if Monster.enemyX[i] <= 0:
            Monster.enemyX_change[i] = 4
            Monster.enemyY[i] += Monster.enemyY_change[i]
        elif Monster.enemyX[i] >= 736:
            Monster.enemyX_change[i] = -4
            Monster.enemyY[i] += Monster .enemyY_change[i]
        # collision
        collision = iscollision(Monster.enemyX[i], Monster.enemyY[i], bullet.bulletX, bullet.bulletY)
        if collision:
            bullet.bulletY = 480
            bullet.bullet_state  = "ready"
            score.score_value += 1
            Monster.enemyX[i] = random.randint(0, 735)
            Monster.enemyY[i] = random.randint(0, 150)
        collision2 = iscollision(man.playerX, man.playerY, Monster.enemyX[i], Monster.enemyY[i])
        if collision2:
            temp = 1
            break
        Monster.showEnemy(Monster.enemyX[i], Monster.enemyY[i], i)
    # bullet movement
    if bullet.bulletY <= 0:
        bullet.bulletY = 480
        bullet.bullet_state = "ready"

    if bullet.bullet_state is "fire":
        bullet.fire_bullet(bullet.bulletX, bullet.bulletY)
        bullet.bulletY -= bullet.bulletY_change
    if score.score_value == 20:
        print("You win")
        break

    man.showPlayer(man.playerX,man.playerY)

    pygame.display.update()
