from random import shuffle
import pygame


def getDefaultRect(x, y):
    return pygame.Rect(x * scaleX, y * scaleY, scaleX, scaleY)


def drawRect(x, y, color=(25, 25, 25)):
    rect = getDefaultRect(x, y)
    pygame.draw.rect(screen, color, rect)


def BFS():
    visited = []
    queue = [start]
    while queue:
        no = queue.pop(0)
        visited.append(no)
        for i in adiciona:
            node_check = [no[0] + i[0], no[1] + i[1]]
            if isnt_within_limits(node_check, goal):
                continue
            if node_check == goal:
                return visited
            verify = allSquares[node_check[0]][node_check[1]]
            if verify == free and node_check not in visited:
                queue.append(node_check)
                visited.append(node_check)

def DFS(no=None, visited = []):
    if not no:
        no = start
    if no not in visited:
        visited.append(no)
        for i in adiciona:
            node_check = [no[0] + i[0], no[1] + i[1]]
            if isnt_within_limits(node_check, goal):
                continue
            if node_check == goal:
                return visited
            verify = allSquares[node_check[0]][node_check[1]]
            if verify == free:
                DFS(node_check, visited)
    return visited


def a_star():
    queue = []
    visited = []
    queue.append([start, 0])
    while queue:
        no = queue[get_min_f(queue)]
        queue.remove(no)
        visited.append(no[0])
        if no[0] == goal:
            return visited
        for i in adiciona:
            node_check = [[no[0][0] + i[0], no[0][1] + i[1]]]
            node_check.append(get_h(node_check[0], goal))
            if isnt_within_limits(node_check[0], goal):
                continue
            if node_check[0] in visited or node_check in queue:
                continue
            verify = allSquares[node_check[0][0]][node_check[0][1]]
            if verify == free:
                queue.append(node_check)


def get_min_f(list):
    lowest = float('inf')
    index = None
    for i in range(len(list)):
        if list[i][1] < lowest:
            index = i
            lowest = list[i][1]
    return index

def get_h(start, end):
    return end[0] - start[0] + end[1] - start[1]


def maze_with_dfs(limit, no=None, visited=[]):
    if not no:
        no = start
    if no not in visited:
        visited.append(no)
        directions = adiciona
        shuffle(directions)
        for dire in directions:
            node_check = [no[0] + dire[0], no[1] + dire[1]]
            if node_check[0] < 0 or node_check[1] < 0 or node_check[0] > limit or node_check[1] > limit:
                continue
            maze_with_dfs(limit, node_check, visited)
    return visited


def isnt_within_limits(node_check, limiter):
    return True if (node_check[0] < 0 or node_check[1] < 0 or node_check[0] > limiter[0] or node_check[1] > limiter[1]) else False


if __name__ == "__main__":

    adiciona = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    wall = '#'
    free = '.'

    allSquares = []
    arquivo = open('input.txt', encoding='utf-8-sig')
    for linha in arquivo.readlines():
        allSquares.append(linha.replace('\n', ''))

    allSquares[-1] += free
    allSquares[-2] += free

    pygame.init()
    width = len(allSquares[-1]) * 15
    height = len(allSquares) * 15
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    scaleX = width / len(allSquares[0])
    scaleY = height / len(allSquares)

    start = [0, 0]
    startRect = getDefaultRect(start[0], start[1])

    goal = [len(allSquares) - 1, len(allSquares[-1]) - 1]
    goalRect = getDefaultRect(goal[1], goal[0])

    vis = []
    # vis = BFS()
    # vis = DFS()
    # vis = a_star()
    
    # vis = maze_with_dfs(50)

    lastDrawn = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i in range(len(allSquares)):
            for j in range(len(allSquares[i])):
                if allSquares[i][j] == wall:
                    drawRect(j, i, (100, 100, 100))

        pygame.draw.rect(screen, (30, 30, 150), startRect)
        pygame.draw.rect(screen, (150, 30, 30), goalRect)

        iter_through = True
        if iter_through:
            for i in range(0, lastDrawn):
                if i < len(vis):
                    draw = vis[i]
                    drawRect(draw[1], draw[0], (0, 130, 0))
                else:
                    iter_through = False
            lastDrawn += 1

        pygame.display.flip()



    pygame.quit()
