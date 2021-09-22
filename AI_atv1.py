sala1 = [0,0]
sala2 = [0,0]
posbot = [0]

def aspirar(sala):
    sala = [1,1]
    return sala

def entrarSala1(posbot):
    posbot[0] = 0
    return posbot

def entrarSala2(posbot):
    posbot[0] = 1
    return posbot

print(entrarSala1(posbot) + aspirar(sala1))

print(entrarSala2(posbot) + aspirar(sala2))
