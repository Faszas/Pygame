import pygame
import time
import random

pygame.init()
pygame.font.init()



class Game:

    def __init__(self):
        self.width = 1000
        self.height = 800
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def displayText(self, y, msg='', size=50, color=(255, 0, 0)):
        font = pygame.font.SysFont('comicsans', size)
        text = font.render(msg, 1, color)
        text_center = text.get_rect(center=(self.width // 2, y))
        self.screen.blit(text, text_center)

    def get_sentence(self):
        return random.choice(open('sentences.txt').read().split('\n'))

    def show_result(self):
        if not self.end:
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.total_time = time.time() - self.time_start ## tinh thoi gian
            self.accuracy = count / len(self.word) * 100
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)

            self.results = "Time: {} secs Accurancy: {}% Wpm: {}".format(round(self.total_time, 2), round(self.accuracy, 2), round(self.wpm))

            print(self.results)
            self.end = True
            self.displayText(msg="Reset", y=self.height - 70, size=40, color=(100, 100, 100))
            pygame.display.update()


    def resetgame(self):
        self.reset = False
        self.end = False
        self.input_text = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        self.word = self.get_sentence()
        if not self.word:
            self.resetgame()
        self.screen.fill((0, 0, 0))
        self.displayText(80, msg='Typing Speed Test', size=80, color=self.HEAD_C)
        #input box
        pygame.draw.rect(self.screen, (255, 192, 25), (0, 250, self.width, 50), 2)
        self.displayText(y=200, msg=self.word, size=28, color=self.TEXT_C)
        pygame.display.update()

    def run(self):
        global count
        self.resetgame()

        while True:
            self.screen.fill((0, 0, 0), (50, 250, self.width, 50))
            pygame.draw.rect(self.screen, (255, 192, 25), (0, 250, self.width, 50), 2)
            # update the text of user input
            self.displayText(msg=self.input_text, y=274, size=26, color=(250, 250, 250))
            pygame.display.update()
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    # position of input box
                    if pos[0] >= 0 and pos[0] <= self.width and pos[1] >= 250 and pos[1] <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                    if (pos[0]  >= 310 and pos[0]  <= 510 and pos[1]  >= 390 and self.end):
                        self.resetgame()

                elif event.type == pygame.KEYDOWN:

                    if self.active and not self.end:

                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_result()
                            print(self.results)
                            self.displayText(msg=self.results, y=350, size=28, color=self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            self.input_text += event.unicode

            pygame.display.update()
            
Game().run()