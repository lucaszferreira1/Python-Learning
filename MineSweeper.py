from cmath import rect
from random import randint
import sys, pygame
pygame.init()

def createBoard(nBombs):
    bombs = []
    for i in range(10, width - 10, scale):
        for j in range(10, height - 10, scale):
            pygame.draw.rect(screen,  blue, [i, j, scale, scale], 1)
    for i in range(0, nBombs):
        bombs.append([randint(1, (width - scale) / scale) * 20, randint(1, (height - scale) / scale) * 20])
    for i in bombs:
        pygame.draw.circle(screen, [255, 0, 0], i, 5)
    return bombs

def isBomb(position):
    for b in bombs:
        if (position[0] >= (b[0] - 10) and position[0] <= (b[0] + 10)):
            if (position[1] >= (b[1] - 10) and position[1] <= (b[1] + 10)):
                return True
    return False

def countBombsAround(position):
    for i in range(0, 3):
        for j in range(0, 3):
            if (isBomb()):
                print("teste")

scale = 20
size = width, height = 320, 240
blue = 0, 0, 255
black = 0, 0, 0



nBombs = 80

screen = pygame.display.set_mode(size)

bombs = createBoard(nBombs) 


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if (isBomb(pos)):
                pygame.QUIT: sys.exit()
            else:
                countBombsAround(pos)
        
    pygame.display.flip()    
    
