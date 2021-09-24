salas = [0, 0]

posbot = [0]

def aspirar():
    salas[posbot[0] - 1] = 1
    return salas

def entrarSala(sala):
    posbot[0] = sala  
    return posbot

def addSala(salas, status):
    for x in status:
        salas += [x]
    return salas

print(posbot + salas)
print(entrarSala(1) + aspirar())
print(entrarSala(2) + aspirar())
addSala(salas, [0, 0, 1])
print(entrarSala(3) + aspirar())
print(entrarSala(5) + aspirar())
