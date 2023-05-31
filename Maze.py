import pygame

class Square:
    def __init__(self, walls):
        # [North, East, South, West] 
        self.walls = walls
    
    def draw(self, x, y):
        x *= scaleX
        y *= scaleY

        # North
        if self.walls[0] == 1:
            pygame.draw.line(screen, 255, [x, y], [x + scaleX, y], 1)
        # East
        if self.walls[1] == 1:
            pygame.draw.line(screen, 255, [x + scaleX, y], [x + scaleX, y + scaleY], 1)
        # South
        if self.walls[2] == 1:
            pygame.draw.line(screen, 255, [x, y + scaleY], [x + scaleX, y + scaleY], 1)
        # West
        if self.walls[3] == 1:
            pygame.draw.line(screen, 255, [x, y], [x, y + scaleY], 1)

if __name__ == "__main__":
    
    pygame.init()
    width = 720
    height = 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    allSquares = [[Square([1, 0, 0, 1]), Square([1, 0, 0, 0]), Square([1, 0, 0, 0]), Square([1, 1, 0, 0])],
                  [Square([0, 0, 0, 1]), Square([1, 0, 0, 1]), Square([1, 1, 0, 0]), Square([0, 1, 0, 0])],
                  [Square([0, 0, 0, 1]), Square([0, 0, 1, 1]), Square([0, 1, 1, 0]), Square([0, 1, 0, 0])],
                  [Square([0, 0, 1, 1]), Square([0, 0, 1, 0]), Square([0, 0, 1, 0]), Square([0, 1, 1, 0])]]

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
                allSquares[i][j].draw(j, i)

        pygame.draw.rect(screen, (30, 30, 150), startRect)
        pygame.draw.rect(screen, (150, 30, 30), goalRect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    
