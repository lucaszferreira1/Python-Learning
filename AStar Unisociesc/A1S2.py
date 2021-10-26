# Cidades
graph = {
    'SaoMiguel': [['Chapeco',[128,407]]],
    'Chapeco': [['SaoMiguel',[128,502]],['Piratuba',[132,319]]],
    'Piratuba': [['Chapeco',[132,407]], ['TrezeTilias',[98, 291]], ['Lages',[206, 177]]],
    'TrezeTilias': [['Piratuba',[98, 319]], ['Lages',[195, 177]], ['Canoinhas',[227, 242]]],
    'Lages': [['Piratuba',[206,319]], ['TrezeTilias',[195, 291]], ['Blumenau',[216, 97]], ['Urubici',[108, 112]]],
    'Canoinhas': [['TrezeTilias',[227, 291]], ['Blumenau',[226, 97]], ['Joinville',[196, 148]]],
    'Blumenau': [['Lages', [216, 177]], ['Canoinhas',[226, 242]], ['Joinville',[92, 148]], ['Urubici',[214, 112]], ['BalCamboriu',[67, 51]], ['Florianopolis',[144, 0]]],
    'Urubici': [['Lages',[108, 177]], ['Blumenau',[214, 97]], ['Tubarao',[104, 109]], ['Criciuma',[153, 146]]],
    'Joinville': [['Canoinhas', [196, 242]], ['Blumenau',[92, 97]], ['BalCamboriu',[78, 64]]],
    'BalCamboriu': [['Joinville', [103, 148]], ['Blumenau',[67, 97]], ['Florianopolis',[79, 0]]],
    'Tubarao': [['Florianopolis', [141, 0]], ['Urubici',[104, 112]], ['Criciuma',[62, 146]]],
    'Criciuma': [['Urubici', [153, 112]], ['Tubarao',[62, 109]]],
    'Florianopolis': [['BalCamboriu', [78, 64]], ['Blumenau',[144, 97]], ['Tubarao',[141, 109]]]
}
#Função para verificar se a cidade já foi visitada e ordenar as próximas cidades a serem analisadas
def sorter(visitar, visitados, s):
    for x in graph[s[0]]:
        soma = (x[1][0] + x[1][1])
        if x not in visitados:
            visitar.append([x[0], soma])
    n = len(visitar)
    # Código de Ordenação de Santiago Valdarrama (https://realpython.com/sorting-algorithms-python/){
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if visitar[j][1] > visitar[j + 1][1]:
                visitar[j], visitar[j + 1] = visitar[j + 1], visitar[j]
                already_sorted = False
        if already_sorted:
            break
    # }
    return visitar


# Código de busca A*
def BuscaAStar(inicial):
    visitados = []
    caminho = []
    visitar = [inicial]
    while visitar:
        s = visitar.pop(0)
        if s[0] == 'Florianopolis':
            return 'Melhor Caminho '+str(caminho + [s[0]])
        caminho.append(s[0])
        visitar = sorter(visitar, visitados, s)
        visitados.append(s)
    return False

print('De onde vocë quer partir?')
print('SaoMiguel, Chapeco, Piratuba, TrezeTilias, Lages, Canoinhas, Blumenau, Urubici, Joinville, BalCamboriu, Tubarao, Criciuma')
inicial = input()
# Caso seja necessário descomente a próxima linha e comente a de cima para testar
# inicial = 'SaoMiguel'
print(BuscaAStar([inicial]))