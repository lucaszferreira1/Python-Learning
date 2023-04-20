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

def BFS(startpos, endpos):
    queue = []
    visited = []
    graph = {}
    queue.append(startpos)
    visited.append(startpos)
    while queue:
        s = queue.pop(0)
        moves_s = knight_moves(s)
        temp_dict = {s:moves_s}
        graph = graph | temp_dict
        for i in moves_s:
            if i == endpos:
                return graph
            if i not in visited:
                queue.append(i)
                visited.append(i)
    
    
    
        
# print(knight_moves('b1'))  # Returns {'a3', 'c3', 'd2'}
# print(knight_moves('e5'))  # Returns {'d7', 'f7', 'c4', 'g4', 'c6', 'g6', 'd3', 'f3'}
# print(knight_moves('x1'))  # Returns set()

print(knight_shortest_path('b1', 'b3'))
    
