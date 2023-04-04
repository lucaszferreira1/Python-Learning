class AFD:
    def __init__(self, alfabeto, estados, funcao, inicial, finais):
        self.A = alfabeto
        self.Q = estados
        self.D = funcao
        self.qi = inicial
        self.F = finais
    
    def getOptions(self, pos):
        return self.D[pos]
    

def navigate(palavra, posAtual, letraAtual, tempPalavra, finais):
    tempPos = 0
    
    if palavra == tempPalavra and posAtual in finais:
        return True
    if len(tempPalavra) >= len(palavra):
        return False
    for i in auto.D[posAtual]:
        for c in i:
            if c != '' and c == palavra[letraAtual]:
                if navigate(palavra, tempPos, letraAtual + 1, tempPalavra + c, finais):
                    return True
        tempPos += 1
    return False

if __name__ == "__main__":
    # auto = AFD("ab", [0, 1, 2], [['', 'a', ''], ['', '', 'b'], ['a', '', 'a']], 0, [2])
    # auto = AFD("ab", [0, 1, 2, 3], [["", "a", "b", ""], ["", "", "b", "a"], ["", "a", "", "b"],["", "", "", "ab"]], 0, [3])
    
    # print(navigate('', auto.qi, 0, "", auto.F))
