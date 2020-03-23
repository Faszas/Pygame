import pygame

width, height = 800, 417
window = pygame.display.set_mode((width, height))

background = pygame.image.load('images/bg.png')
pygame.display.set_caption('scrolling background')
bgX = 0
bgX2 = background.get_width()


class PLAYER(object):


    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.status = 'run'
        self.imgCurrentStatus = pygame.image.load('images/S5.png')
        self.playerImg = [pygame.image.load('images/{}.png'.format(x)) for x in range(7, 16)]
        self.count = 0
        self.imgSilde = pygame.image.load('images/S2.png')
        self.countSliding = 0

    def display(self):
        if self.status == 'ready':
            window.blit(self.imgCurrentStatus, (self.x, self.y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.status = 'sliding'

        if self.status == 'run':
            self.x += self.vel
            if self.count >= len(self.playerImg):
                self.count = 0
            window.blit(self.playerImg[self.count], (self.x, self.y))
            self.count += 1
        
        if self.x >= width - 50:
            self.x = width - 50

        if self.status == 'sliding':
            self.x += self.vel
            window.blit(self.imgSilde, (self.x, self.y+30))
            self.countSliding += 1
            if self.countSliding > 10 :
                self.status = 'run'
        
            

player = PLAYER(30, height - 110, 5)

def display():
    window.blit(background, (bgX, 0))
    window.blit(background, (bgX2, 0))
    player.display()
    pygame.display.update()


while True:
    display()
    pygame.time.Clock().tick(30)

    bgX -= 16  # Move both background images back
    bgX2 -= 16

    if bgX < background.get_width() * -1:
        bgX = background.get_width()
    
    if bgX2 < background.get_width() * -1:
        bgX2 = background.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    display()

