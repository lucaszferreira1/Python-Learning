import pygame

if __name__ == "__main__":
    
    pygame.init()
    width = 720
    height = 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    allSquares = [[0,0,0,0],
                  [0,1,1,0],
                  [0,1,1,0],
                  [0,0,0,0],]

    scaleX = width / len(allSquares)
    scaleY = height / len(allSquares[0])

    start = [0, 0]
    startRect = pygame.Rect(start[0] * scaleX, start[1] * scaleY, scaleX, scaleY)

    goal = [3, 3]
    goalRect = pygame.Rect(goal[0] * scaleX, goal[1] * scaleY, scaleX, scaleY)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i in range(len(allSquares)):
            for j in range(len(allSquares[i])):
                if allSquares[i][j]:
                    pygame.draw.rect(screen, (100, 100, 100), (i * scaleX, j * scaleY, scaleX, scaleY))

        pygame.draw.rect(screen, (30, 30, 150), startRect)
        pygame.draw.rect(screen, (150, 30, 30), goalRect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    
