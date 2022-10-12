from cmath import rect
from random import randint, sample
import sys, pygame

pygame.init()

def drawRects():
    s = int(scale / 2)
    for i in range(s, width - s, scale):
        for j in range(s, height - s, scale):
            pygame.draw.rect(screen, blue, [i, j, scale, scale], 1)


def getArea():
    return int(((width - scale) / scale) * ((height - scale) / scale))


def inScreen(position):
    return True if (scale / 2 < position[0] < width - scale / 2) and (scale / 2 < position[1] < height - scale / 2) else False


def createBoard(nBombs):
    drawRects()
    bombs = []
    bomb_samples = sample(range(getArea()), nBombs)
    if 0 in bomb_samples:
        bomb_samples.remove(0)
        for n in range(1, nBombs):
            if n not in bomb_samples:
                bomb_samples.append(n)
                break
    cont = 0
    for i in range(1, int(width / scale)):
        for j in range(1, int(height / scale)):
            if cont in bomb_samples:
                   bombs.append([i * scale, j * scale])
            cont += 1
    # for i in bombs:
    #     pygame.draw.circle(screen, [255, 0, 0], i, 5 * (scale / 20))
    return bombs


def isBomb(position):
    for b in bombs:
        if b[0] - scale / 2 <= position[0] <= b[0] + scale / 2:
            if b[1] - scale / 2 <= position[1] <= b[1] + scale / 2:
                return True
    return False


def getIndexOfBomb(pos):
    pos = fixPosition(pos)
    return bombs.index([pos[0] + 80, pos[1] + 80])


def countBombsAround(position):
    aroundbombs = 0
    for i in range(-scale, scale * 2, scale):
        for j in range(-scale, scale * 2, scale):
            if isBomb((position[0] + i, position[1] + j)):
                aroundbombs += 1
    return aroundbombs


def fixPosition(position):
    position = (position[0] - scale / 2, position[1] - scale / 2)
    position = (position[0] - (position[0] % scale), position[1] - (position[1] % scale))
    return position


def drawNumberOfBombs(aroundbombs, position, checkedspaces = []):
    if aroundbombs > 0 and inScreen(position):
        position = fixPosition(position)
        nmbr = font.render(str(aroundbombs), True, nmbr_colors[aroundbombs - 1])
        screen.blit(nmbr, (position[0] + (scale * 0.75), position[1] + (scale * 0.6)))
    else:
        for i in range(-scale, scale*2, scale):
            for j in range(-scale, scale*2, scale):
                pos = position[0] + i, position[1] + j
                if position != pos and not isBomb(pos) and pos not in checkedspaces and inScreen(pos) and not hasFlag(pos):
                    checkedspaces.append(pos)
                    pygame.draw.rect(screen, beige, [fixPosition(pos)[0] + scale / 2, fixPosition(pos)[1] + scale / 2, scale, scale], 0)
                    drawNumberOfBombs(countBombsAround(pos), pos, checkedspaces)


def hasFlag(position):
    return True if (fixPosition(position) in flags) else False


def placeFlag(pos):
    pos = fixPosition(pos)
    triangle = [[pos[0] + (scale * 0.8), pos[1] + (scale * 0.7)], [pos[0] + (scale * 1.15), pos[1] + (scale * 0.85)], [pos[0] + (scale * 0.8), pos[1] + scale]]
    flags.append(pos)
    pygame.draw.rect(screen, beige, [pos[0] + scale / 2, pos[1] + scale / 2, scale, scale], 0)
    pygame.draw.line(screen, black, [pos[0] + (scale * 0.8), pos[1] + (scale * 0.75)], [pos[0] + (scale * 0.8), pos[1] + (scale * 1.45)], 2)
    pygame.draw.polygon(screen, red, triangle, 0)


def removeFlag(position):
    position = fixPosition(position)
    flags.remove(position)
    pygame.draw.rect(screen, black, [position[0] + scale / 2, position[1] + scale / 2, scale, scale], 0)
    pygame.draw.rect(screen, blue, [position[0] + scale / 2, position[1] + scale / 2, scale, scale], 1)


def checkBombsWindowSize():
    return True if getArea() > nBombs else False


def hasFlaggedBomb(pos):
    return True if isBomb(pos) else False


scale = 40
size = width, height = 1280, 720
blue = 0, 0, 255
black = 0, 0, 0
beige = 200, 200, 200
red = 255, 0, 0
nmbr_colors = [blue, (0, 200, 0), red, (106, 13, 173), (128, 0, 0), (24, 184, 168), black, (72, 72, 72)]

nBombs = 100

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, int(scale * 1.5))
bombs = createBoard(nBombs)
flags = []
first = True
flaggedBombs = 0
flaggedBlanks = 0

if checkBombsWindowSize():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if inScreen(pos):
                    if event.button == 1:
                        if not hasFlag(pos):
                            if first:
                                if isBomb(pos):
                                    bombs[getIndexOfBomb(pos)] = [80, 80]
                                pygame.draw.rect(screen, beige, [fixPosition(pos)[0] + scale / 2, fixPosition(pos)[1] + scale / 2, scale,scale], 0)
                                drawNumberOfBombs(countBombsAround(pos), pos)
                                first = False
                            elif isBomb(pos):
                                print("YOU LOSE!")
                                pygame.QUIT: sys.exit()
                            else:
                                pygame.draw.rect(screen, beige,[fixPosition(pos)[0] + scale / 2, fixPosition(pos)[1] + scale / 2, scale, scale], 0)
                                drawNumberOfBombs(countBombsAround(pos), pos)
                    elif event.button == 3:
                        if hasFlag(pos):
                            removeFlag(pos)
                            if hasFlaggedBomb(pos):
                                flaggedBombs -= 1
                            else:
                                flaggedBlanks -= 1
                        else:
                            placeFlag(pos)
                            if hasFlaggedBomb(pos):
                                flaggedBombs += 1
                            else:
                                flaggedBlanks += 1

        if nBombs == flaggedBombs and flaggedBlanks == 0:
            print("YOU WIN!")
            break
        pygame.display.flip()
