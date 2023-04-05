class AFD:
    def __init__(self, alfabeto, estados, funcao, inicial, finais):
        self.A = alfabeto
        self.Q = estados
        self.D = funcao
        self.qi = inicial
        self.F = finais

    def __str__(self):
        return (self.A, self.Q, self.D, self.qi, self.F)


def navigate(auto, palavra, posAtual, letraAtual, tempPalavra, finais):
    tempPos = 0

    if palavra == tempPalavra and posAtual in finais:
        return True
    if len(tempPalavra) >= len(palavra):
        return False
    for i in auto.D[posAtual]:
        for c in i:
            if c != '' and c == palavra[letraAtual]:
                if navigate(auto, palavra, tempPos, letraAtual + 1, tempPalavra + c, finais):
                    return True
        tempPos += 1
    return False

if __name__ == "__main__":

    # Automatos
    # Baseados nos exercícios vistos em sala de aula e slide de AFD
    auto0 = AFD("ab", [0, 1, 2, 3], [["", "a", "b", ""], ["", "", "b", "a"], ["", "a", "", "b"],["", "", "", "ab"]], 0, [3])
    auto1 = AFD("abcd", [0, 1, 2], [["ab", "c", "d"], ["cab", "", "d"], ["", "dcab", ""]], 0, [0,1])
    auto2 = AFD("abc", [0, 1, 2, 3], [["c", "", "a", "b"], ["a", "", "", "bc"], ["", "", "b", "ac"], ["", "", "b", "ab"]], 0, [2, 3])
    auto3 = AFD("abc", [0, 1, 2, 3], [["", "a", "c", "a"], ["ab", "b", "", ""], ["", "b", "", "a"], ["", "", "", "c"]], 0, [1, 3])
    # Gerado com o website http://ivanzuzak.info/noam/webapps/fsm_simulator/
    auto4 = AFD("abc", [0, 1, 2, 3], [["a", "c", "", ""], ["a", "", "c", "ab"], ["", "ab", "b", "a"], ["", "bc", "", "bc"]], 0, [2, 3])

    automatos = [auto0, auto1, auto2, auto3, auto4]

    escolha = int(input("Escolha o automato(0 - 4): "))
    
    palavra = input("Digite a palavra: ")

    print(navigate(automatos[escolha], palavra, automatos[escolha].qi, 0, "", automatos[escolha].F))
