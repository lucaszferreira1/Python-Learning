import pygame

def getDefaultRect(x, y):
    return pygame.Rect(x * scaleX, y * scaleY, scaleX, scaleY)

def drawRect(x, y, color = (25, 25, 25)):
    rect = getDefaultRect(x, y)
    pygame.draw.rect(screen, color, rect)

def BFS():
    add = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    visited = []
    queue = [start]
    while(queue):
        no = queue.pop(0)
        visited.append(no)
        for i in add:
            nodeCheck = [no[0] + i[0], no[1] + i[1]]
            if nodeCheck[0] < 0 or nodeCheck[1] < 0:
                continue
            verify = allSquares[nodeCheck[0]][nodeCheck[1]]
            if nodeCheck == goal:
                return visited
            if verify == free and nodeCheck not in visited:
                queue.append(nodeCheck)
                visited.append(nodeCheck)


if __name__ == "__main__":
    
    pygame.init()
    width = 820
    height = 820
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    allSquares = ["  ###################",
                  "      #     #   #   #",
                  "### ### # ### # # # #",
                  "# #   # #     #   # #",
                  "# ### ### ### ##### #",
                  "#   #   #   # #     #",
                  "# # # ####### ### ###",
                  "# #   # #   # #     #",
                  "##### # # # # # #####",
                  "# #       #   #     #",
                  "# # ##### # #########",
                  "#   #     #         #",
                  "# # # ### ###########",
                  "# # #   # #     #   #",
                  "####### # # ### ### #",
                  "# # # # #     # # # #",
                  "# # # ####### ### # #",
                  "# # #   # # #   #   #",
                  "# # # # # # # ### # #",
                  "#     #           #  ",
                  "###################  "]

    scaleX = width / len(allSquares[0])
    scaleY = height / len(allSquares)

    start = [0, 0]
    startRect = getDefaultRect(start[0], start[1])
    
    goal = [len(allSquares) - 1, len(allSquares[:-1]) - 1]
    goalRect = getDefaultRect(goal[0], goal[1])

    wall = '#'
    free = ' '
    
    visited = BFS()
    lastDrawn = 0
    print(visited)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i in range(len(allSquares)):
            for j in range(len(allSquares[i])):
                if allSquares[i][j] == wall:
                    pygame.draw.rect(screen, (100, 100, 100), (j * scaleX, i * scaleY, scaleX, scaleY))

        pygame.draw.rect(screen, (30, 30, 150), startRect)
        pygame.draw.rect(screen, (150, 30, 30), goalRect)
        
        pygame.display.flip()

        for i in range(0, lastDrawn):
            draw = visited[i]
            drawRect(draw[0], draw[1], (0, 130, 0))
            lastDrawn += 1
        

        clock.tick(10)

    pygame.quit()
    
