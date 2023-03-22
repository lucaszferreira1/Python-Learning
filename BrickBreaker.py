import pygame
from random import randint

width = 1280
height = 720

class Ball:
    def __init__(self, size, speed, color, directions, position):
        self.size = size
        self.speed = speed
        self.color = color
        self.dir = directions
        self.pos = position
    
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size[0], self.size[1])
    
    def checkCollisionScreen(self):
        if (self.pos[0] <= self.size[0] or self.pos[0] >= (width - self.size[0])):
            self.dir[0] *= -1
        if (self.pos[1] <= self.size[1] or self.pos[1] >= (height - self.size[0])):
            self.dir[1] *= -1
    
    def checkCollisionBrick(self, bricks):
        for brick in bricks:
            if ((self.pos[0] >= brick.pos[0]) and (self.pos[0] <= brick.pos[0] + brick.size[0]) and (self.pos[1] >= brick.pos[1]) and (self.pos[1] <= brick.pos[1] + brick.size[1])):
                self.dir[0] *= -1
                self.dir[1] *= -1
    
    def move(self):
        self.pos[0] = self.pos[0] + (self.speed * self.dir[0])
        self.pos[1] = self.pos[1] + (self.speed * self.dir[1])

class Brick:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.size[0], self.size[1]])
    

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball1 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])
ball2 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])
ball3 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])
ball4 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])
ball5 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])
ball6 = Ball([10, 10], 5, "white", [1, 1], [randint(10, 1270), randint(10, 710)])

brick1 = Brick([randint(0, 1180), randint(0, 620)], [100, 100], "white")

allBricks = [brick1]
allBalls = [ball1, ball2, ball3, ball4, ball5, ball6]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for ball in allBalls:
        ball.draw()
        ball.checkCollisionScreen()
        ball.move()
        ball.checkCollisionBrick(allBricks)
    
    for brick in allBricks:
        brick.draw()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()