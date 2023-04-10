import pygame

class Piece:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

pygame.init()
widhei = 540
scale = widhei / 8
screen = pygame.display.set_mode((widhei, widhei))
clock = pygame.time.Clock()
running = True
whiteColor = (238,238,210)
blackColor = (118,150,86)

board = [[Piece("Rook", "black", 5), Piece("Knight", "black", 3), Piece("Bishop", "black", 3), Piece("Queen", "black", 9), Piece("King", "black", 0), Piece("Bishop", "black", 3), Piece("Knight", "black", 3), Piece("Rook", "black", 5)], [Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1)], [], [], [], [], [Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1)], [Piece("Rook", "white", 5), Piece("Knight", "white", 3), Piece("Bishop", "white", 3), Piece("Queen", "white", 9), Piece("King", "white", 0), Piece("Bishop", "white", 3), Piece("Knight", "white", 3), Piece("Rook", "white", 5)]]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board
    screen.fill(blackColor)
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            pygame.draw.rect(screen, whiteColor, [scale*i, scale*j, scale, scale])
    for i in range(1, 8, 2):
        for j in range(1, 8, 2):
            pygame.draw.rect(screen, whiteColor, [scale*i, scale*j, scale, scale])
    
    # Draw the pieces on the board
    for i in range(0, 8):
        if len(board[i]) > 0:
            for j in range(0, 8):
                if board[i][j]:
                    p = board[i][j]
                    img = pygame.image.load("Chess\chessIcons\p"+p.color+p.name+".png")
                    screen.blit(img, (j*scale+3, i*scale+4))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
