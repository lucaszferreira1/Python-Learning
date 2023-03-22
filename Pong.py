import pygame

# pygame setup
pygame.init()
pygame.key.set_repeat(10, 10)
width = 1280
height = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ballSpe = 5
wallSpe = 5
direction = [1, 1]

circSize = [10, 10]
circPos = [150, 150]

rectPos1 = [80, 360]
rectPos2 = [1200, 360]
rectSize = [25, 100]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rectPos1[1] -= wallSpe
            if event.key == pygame.K_s:
                rectPos1[1] += wallSpe

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    
    pygame.draw.rect(screen, "white", [rectPos1[0], rectPos1[1], rectSize[0], rectSize[1]])
    pygame.draw.rect(screen, "white", [rectPos2[0], rectPos2[1], rectSize[0], rectSize[1]])
    pygame.draw.circle(screen, "white", circPos, circSize[0], circSize[1])
    
    if (circPos[0] <= circSize[0] or circPos[0] >= (width - circSize[0])):
        direction[0] *= -1
    if (circPos[1] <= circSize[1] or circPos[1] >= (height - circSize[0])):
        direction[1] *= -1
    
    circPos[0] = circPos[0] + (ballSpe * direction[0])
    circPos[1] = circPos[1] + (ballSpe * direction[1])
    
    
    if ((circPos[0] >= rectPos1[0]) and (circPos[0] <= rectPos1[0] + rectSize[0]) and (circPos[1] >= rectPos1[1]) and (circPos[1] <= rectPos1[1] + rectSize[1])):
        direction[0] *= -1
        if (circPos[1] <= rectPos1[1] + (rectSize[1] / 2)):
            direction[1] = -1
        else:
            direction[1] = 1
    if ((circPos[0] >= rectPos2[0]) and (circPos[0] <= rectPos2[0] + rectSize[0]) and (circPos[1] >= rectPos2[1]) and (circPos[1] <= rectPos2[1] + rectSize[1])):
        direction[0] *= -1
        if (circPos[1] <= rectPos2[1] + (rectSize[1] / 2)):
            direction[1] = -1
        else:
            direction[1] = 1

    if (circPos[1] > rectPos2[1] + (rectSize[1] / 2)):
        rectPos2[1] += wallSpe
    elif (circPos[1] < rectPos2[1] + (rectSize[1] / 2)):
        rectPos2[1] -= wallSpe

    if (rectPos1[1] + rectSize[1] > height):
        rectPos1[1] = height - rectSize[1]
    elif (rectPos1[1] < 0):
        rectPos1[1] = 0
        
    if (rectPos2[1] + rectSize[1] > height):
        rectPos2[1] = height - rectSize[1]
    elif (rectPos2[1] < 0):
        rectPos2[1] = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()