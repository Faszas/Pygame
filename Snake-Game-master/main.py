import pygame
import random
class SNAKE:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.snakeList = []
        self.snakeLength = 1
        self.size = 20
        self.vel = 10
    def move(self, iscollison, window):
        def showSnake(window, size, snakeList):
            for i in snakeList:
                pygame.draw.rect(window, (255, 0, 0), (i[0], i[1], size, size))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_change = self.vel
            self.y_change = 0
        elif keys[pygame.K_LEFT]:
            self.x_change = -self.vel
            self.y_change = 0
        elif keys[pygame.K_UP]:
            self.y_change = -self.vel
            self.x_change = 0
        elif keys[pygame.K_DOWN]:
            self.y_change = self.vel
            self.x_change = 0
        self.x += self.x_change
        self.y += self.y_change
        pHead = [self.x, self.y]
        self.snakeList.append(pHead)
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList[0]
        for x in self.snakeList[:-1]:
            if x == pHead:
                quit()
        showSnake(window, self.size, self.snakeList)
        pygame.display.update()
        if self.x > 600:
            self.x = 0
        elif self.x < 0:
            self.x = 600
        elif self.y > 600:
            self.y = 0
        elif self.y < 0:
            self.y = 600
        if iscollison:
            self.snakeLength += 1
class FOOD(SNAKE):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
    def showFOOD(self, window, isCollison):
        pygame.draw.circle(window, (0, 255, 0), (self.x, self.y), self.radius)
        if isCollison:
            self.x = random.randint(30, 570)
            self.y = random.randint(30, 570)
if __name__ == '__main__':
    window = pygame.display.set_mode((600, 600))
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Snake Game')
    snake = SNAKE(random.randint(30, 570), random.randint(30, 570))
    food = FOOD(random.randint(30, 570), random.randint(30, 570))
    isColiision = lambda x1, x2, y1, y2: (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2) < 20
    score_font = pygame.font.SysFont("comicsansms", 35)
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, (0, 0, 255))
        window.blit(value, [0, 0])
    def display():
        temp = isColiision(snake.x, food.x, snake.y, food.y)
        snake.move(temp, window)
        food.showFOOD(window, temp)
        Your_score(snake.snakeLength - 1)
        pygame.display.update()
    while True:
        clock.tick(17)
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        display()


