import pygame
import random


pygame.init()
pygame.font.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("images.jpg"))
pygame.display.set_caption("Snake made by Xuan Hung")
speed = 40
Score = 0

# High_Scores

def displayText(string, text_size, color, posx, posy, win):
    font = pygame.font.SysFont('comicsans', text_size)
    text = font.render(string, 1, color)
    win.blit(text, (posx, posy))

def StorageHighScore():
    global Score
    file_read = open('highScore.txt', 'r')
    temp = file_read.read()
    file_read.close()
    
    file_write = open('highScore.txt', 'w')
    if Score > int(temp):
        file_write.write(str(Score))
    else:
        file_write.write(temp)
    file_write.close()

class BUTTON:


    def __init__(self, x, y, width, height, string="", color=(255, 0, 0) ,textColor=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.string = string
        self.color = color
        self.textColor = textColor
    
    def display(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        displayText(self.string, 30, self.textColor, self.x + self.width // 2 - len(self.string) * 5, self.y + 16, screen)

    def Clicked(self, pos):
        return  pos[0] >= self.x and pos[0] <= self.x  + self.width and pos[1] >= self.y and pos[1] <= self.y + self.height

class SNAKE:
    

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.size = size
        self.color = (255, 0, 0)
        self.snakeBody = []
        self.snakeLength = 1

    def Control(self, win, isCollision):
        def display(win, color, size, snakeBody):
            for block in snakeBody:
                pygame.draw.rect(win, color, (block[0], block[1], size, size))
                
        pHead = [self.x, self.y]
        self.snakeBody.append(pHead)
        
        if len(self.snakeBody) > self.snakeLength:
            del self.snakeBody[0]

        for x in self.snakeBody[:-1]:
            if x == pHead:
                StorageHighScore()
                Pauseloop()

        display(win, self.color, self.size, self.snakeBody)

        # Control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.xchange = 0
            self.ychange = -5
        elif keys[pygame.K_DOWN]:
            self.xchange = 0
            self.ychange = 5
        elif keys[pygame.K_LEFT]:
            self.xchange = -5
            self.ychange = 0
        elif keys[pygame.K_RIGHT]:
            self.xchange = 5
            self.ychange = 0
        self.x += self.xchange
        self.y += self.ychange

        # Check Collision with wall
        if self.x > width + self.size:
            self.x = 0
        if self.x < 0 - self.size:
            self.x = width
        if self.y > height + self.size:
            self.y = 0
        if self.y < 0 - self.size:
            self.y = height
        
        # Check add body block
        if isCollision:
            self.snakeLength += 1
        
            
class FOOD(SNAKE):


    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.color = (0, 255, 255)

    def display(self, win, isCollision):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)
        if isCollision:
            global Score
            self.x = random.randrange(20, width)
            self.y = random.randrange(20, height)
            Score += 1


# button init
btn_start = BUTTON(width // 2 - 120, height // 2 - 200, 250, 50, 'START')
btn_level = BUTTON(btn_start.x, btn_start.y + 80, 250, 50, 'LEVEL')
btn_highscore = BUTTON(btn_level.x, btn_level.y + 80, 250, 50, 'HIGH SCORE')
btn_exit = BUTTON(btn_highscore.x, btn_highscore.y + 80, 250, 50, 'EXIT')
# snake init
snake = SNAKE(random.randrange(20, width), random.randrange(20, height), 30)
# food init
food = FOOD(random.randrange(20, width), random.randrange(20, height), 10)
# level button

btn_easy = BUTTON(width // 2 - 120, height // 2 - 200, 250, 50, 'EASY')
btn_medium = BUTTON(btn_easy.x, btn_easy.y + 80, 250, 50, 'MEDIUM')
btn_hard = BUTTON(btn_medium.x, btn_medium.y + 80, 250, 50, 'HARD')
btn_hardest = BUTTON(btn_hard.x, btn_hard.y + 80, 250, 50, 'HARDEST')
# Back button 
back = BUTTON(btn_hardest.x, btn_hardest.y + 80, 250, 50, 'BACK')

def display_Clicked_level():
    win.fill((0, 0, 0))
    displayText("You have select successfully ! ", 50, (255, 255, 255), width // 2 - 230, height // 2 - 50, win)
    back.display(win)
    pygame.display.update()

def display_Clicked_level_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.Clicked(pos):
                    submainloop()
        display_Clicked_level()

def display_level(win):
    win.fill((0, 0, 0))
    btn_easy.display(win)
    btn_medium.display(win)
    btn_hard.display(win)
    btn_hardest.display(win)
    back.display(win)

    pygame.display.update()

def levelLoop():
    global speed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_easy.Clicked(pos):
                    speed = 27
                    display_Clicked_level_loop()
                elif btn_medium.Clicked(pos):
                    speed = 47
                    display_Clicked_level_loop()
                elif btn_hard.Clicked(pos):
                    speed = 60
                    display_Clicked_level_loop()
                elif btn_hardest.Clicked(pos):
                    speed = 100
                    display_Clicked_level_loop()
                elif back.Clicked(pos):
                    submainloop()

        display_level(win)

def displayScore(win):
    global Score
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render("Score: " + str(Score), 1, (255, 0, 0))
    win.blit(text, (width - 170, 30))

def isCollision(x1, y1, size1, x2, y2, size2):
    return x1 + size1 >= x2 and x2 + size2 >= x1 and y1 + size1 >= y2 and y2 + size2 >= y1 

def display_HighScore():
    win.fill((0, 0, 0))
    with open("highScore.txt", "r") as f:
        displayText("High Score: " + f.read(), 50, (255, 0, 0), width // 2 - 100, height // 2 - 30, win)
    back.display(win)
    pygame.display.update()

def HighScoreloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                StorageHighScore()
                quit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.Clicked(pos):
                    submainloop()
        display_HighScore()

def display_mainloop():
    win.fill((0, 0, 0))
    temp = isCollision(snake.x, snake.y, snake.size, food.x, food.y, food.size)
    snake.Control(win, temp)
    food.display(win, temp)
    displayScore(win)
    pygame.display.update()


def mainloop():
    global speed
    while True:
        pygame.time.Clock().tick(speed)
        speed += 0.01
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        display_mainloop()

def display_Pauseloop():
    displayText("Click me to continue", 50, (255, 255, 255), width // 2 - 100, height // 2 - 30, win)
    pygame.display.update()

def Pauseloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                StorageHighScore()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                submainloop()
        display_Pauseloop()

def display_submain():
    win.fill((0, 0, 0))
    btn_start.display(win)
    btn_level.display(win)
    btn_highscore.display(win)
    btn_exit.display(win)
    pygame.display.update()

def submainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                StorageHighScore()
                quit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.Clicked(pos):
                    mainloop()
                elif btn_highscore.Clicked(pos):
                    HighScoreloop()
                elif btn_level.Clicked(pos):
                    levelLoop()

                elif btn_exit.Clicked(pos):
                    StorageHighScore()
                    quit()
        display_submain()

if __name__ == "__main__":
    
    submainloop()
