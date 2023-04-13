import pygame

# Draws the board of the game and the pieces in the board
def drawBoard(screen, scale, whiteColor, blackColor, board):
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


# Draws a circle to represent the possible moves a piece can make
def drawSelected(positions):
    for pos in positions:
        pygame.draw.circle(screen, 'red', [pos[0]*scale+scale/2, pos[1]*scale+scale/2], 15)
    

class Move:
    def __init__(self, piece, posfrom , posto):
        self.piece = piece
        self.posfrom = posfrom
        self.posto = posto
    
    

class Piece:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def __str__(self) -> str:
        return self.color.capitalize() + " " + self.name
    # Returns the moves that piece can do, at the end it checks if any of the moves is illegal or impossible
    def get_moves(self, pos, board):
        moves = []
        if self.name == "Pawn":
            if board[pos[1] + intcolor][pos[0]]:
                pass
            elif not board[pos[1] + intcolor + intcolor][pos[0]]:
                moves.append([pos[0], pos[1] + intcolor + intcolor])
            if not board[pos[1] + intcolor][pos[0]]:
                moves.append([pos[0], pos[1] + intcolor])
            if 0 <= pos[0] + intcolor <= 7:
                if board[pos[1] + intcolor][pos[0] + intcolor] != '' and board[pos[1] + intcolor][pos[0] + intcolor].color != self.color:
                    moves.append([pos[0] + intcolor, pos[1] + intcolor])
            if 0 <= pos[0] - intcolor <= 7:
                if board[pos[1] + intcolor][pos[0] - intcolor] != '' and board[pos[1] + intcolor][pos[0] - intcolor].color != self.color:
                    moves.append([pos[0] - intcolor, pos[1] + intcolor])
            
        for move in moves:
            if isOutOfBounds(move):
                moves.remove(move)
        return moves

# Receives the pos of the piece and gets the int values for x and y
def translateXY(pos, scale):
    newpos = [-1, -1]
    newpos[0] = int((pos[0] - (pos[0] % scale)) / scale)
    newpos[1] = int((pos[1] - (pos[1] % scale)) / scale)
    return newpos

# Verify if piece is in or out of bounds, if out it returns True, else False
def isOutOfBounds(pos):
    return True if 0 > pos[0] > 7 and 0 > pos[1] > 7 else False 


def moveTo(move):
    board[move.posto[1]][move.posto[0]] = move.piece
    board[move.posfrom[1]][move.posfrom[0]] = ''


pygame.init()
widhei = 540
scale = widhei / 8
screen = pygame.display.set_mode((widhei, widhei))
clock = pygame.time.Clock()
running = True

# Colors used for the board
whiteColor = (238,238,210)
blackColor = (118,150,86)

# The board containing all the pieces
board = [
    [Piece("Rook", "black", 5), Piece("Knight", "black", 3), Piece("Bishop", "black", 3), Piece("Queen", "black", 9), Piece("King", "black", 0), Piece("Bishop", "black", 3), Piece("Knight", "black", 3), Piece("Rook", "black", 5)],
    [Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1), Piece("Pawn", "black", 1)],
    ['', '', Piece("Queen", "white", 1), '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', Piece("Pawn", "black", 1), ''],
    ['', '', Piece("Pawn", "black", 1), '', '', '', '', ''],
    [Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1), Piece("Pawn", "white", 1)],
    [Piece("Rook", "white", 5), Piece("Knight", "white", 3), Piece("Bishop", "white", 3), Piece("Queen", "white", 9), Piece("King", "white", 0), Piece("Bishop", "white", 3), Piece("Knight", "white", 3), Piece("Rook", "white", 5)]]

squareselected = []
movesDone = []
oldSelection = []
currentturn = 'w'


# Main Loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousepos = translateXY(pygame.mouse.get_pos())
            if board[mousepos[1]][mousepos[0]] and board[mousepos[1]][mousepos[0]].color[0] == currentturn:
                oldSelection = mousepos
                newselection = board[mousepos[1]][mousepos[0]].get_moves(mousepos)
                if newselection != squareselected:
                    squareselected = newselection
                else:
                    squareselected = []
            else:
                print(mousepos)
                lastmove = Move(board[oldSelection[0]][oldSelection[1]], oldSelection, mousepos)
                moveTo(lastmove)
                movesDone.append(lastmove)


    drawBoard()

    if squareselected:
        drawSelected(squareselected)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
