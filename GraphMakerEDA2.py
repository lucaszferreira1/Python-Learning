import matplotlib.pyplot as plt

class Dados:
    def __init__(self, arq):
        arquivo = open(arq)
        self.i = []
        self.n = []
        for linha in arquivo.readlines():
            dados = linha.split(" ")
            self.i.append(int(dados[0]))
            self.n.append(int(dados[1]))


def showGraphInserts():
    dadosAVL = Dados('Inserts\AVLInsert.txt')
    dadosRB = Dados('Inserts\RedBlackInsert.txt')
    dadosBUm = Dados('Inserts\B1Insert.txt')
    dadosBCin = Dados('Inserts\B5Insert.txt')
    dadosBDez = Dados('Inserts\B10Insert.txt')

    plt.plot(dadosAVL.i, dadosAVL.n, color='g', label='AVL')
    plt.plot(dadosRB.i, dadosRB.n, color='r', label='Red Black')
    plt.plot(dadosBUm.i, dadosBUm.n, color='c', label='B (1)')
    plt.plot(dadosBCin.i, dadosBCin.n, color='m', label='B (5)')
    plt.plot(dadosBDez.i, dadosBDez.n, color='y', label='B (10)')

    plt.title("Operações de Insert")


def showGraphRemoves():
    dadosAVL = Dados('Removes\AVLRemove.txt')
    # dadosRB = Dados('Inserts\RedBlackInsert.txt')
    # dadosBUm = Dados('Inserts\B1Insert.txt')
    # dadosBCin = Dados('Inserts\B5Insert.txt')
    # dadosBDez = Dados('Inserts\B10Insert.txt')

    plt.plot(dadosAVL.i, dadosAVL.n, color='g', label='AVL')
    # plt.plot(dadosRB.i, dadosRB.n, color='r', label='Red Black')
    # plt.plot(dadosBUm.i, dadosBUm.n, color='c', label='B (1)')
    # plt.plot(dadosBCin.i, dadosBCin.n, color='m', label='B (5)')
    # plt.plot(dadosBDez.i, dadosBDez.n, color='y', label='B (10)')

    plt.title("Operações de Remove")


if __name__ == "__main__":
    # showGraphInserts()
    showGraphRemoves()
    plt.xlabel("Iterações")
    plt.ylabel("Operações")
    plt.legend()
    plt.show()