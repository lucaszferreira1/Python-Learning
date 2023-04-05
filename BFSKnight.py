def pos_to_int(pos):
    posint = [0, 0]
    posint[0] = ord(pos[0]) - 97
    posint[1] = int(pos[1])
    return posint

def int_to_pos(posint):
    pos = ""
    pos += chr(posint[0] + 97)
    pos += str(posint[1])
    return pos

def knight_moves(pos):
    matrizpos = pos_to_int(pos)
    positions = set()
    for i in range(-2, 4, 4):
        for j in range(-1, 2, 2):
            if 0 <= matrizpos[0] + i <= 8 and 0 < matrizpos[1] + j <= 8:
                positions.add(int_to_pos([matrizpos[0] + i, matrizpos[1] + j]))
            if 0 <= matrizpos[0] + j <= 8 and 0 < matrizpos[1] + i <= 8:
                positions.add(int_to_pos([matrizpos[0] + j, matrizpos[1] + i]))
    return positions

def knight_shortest_path(startpos, endpos, visited = set()):
    moves = BFS(startpos, endpos)

def BFS(startpos, endpos, visited = set()):
    queue = []
    queue.append(startpos)
    visited.add(startpos)
    while queue:
        s = queue.pop(0)
        
        for i in knight_moves(s):
            if i == endpos:
                visited.add(i)
                return
            if i not in visited:
                queue.append(i)
                visited.add(i)
    
    
    
        
# print(knight_moves('b1'))  # Returns {'a3', 'c3', 'd2'}
# print(knight_moves('e5'))  # Returns {'d7', 'f7', 'c4', 'g4', 'c6', 'g6', 'd3', 'f3'}
# print(knight_moves('x1'))  # Returns set()

print(knight_shortest_path('b1', 'b3'))
    
