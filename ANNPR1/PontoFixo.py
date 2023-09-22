from sympy import *
from math import e

def funcao(funcao, xi, tolerancia, kmax):
    k = 0
    Er = tolerancia + 1
    while (k <= kmax) and (Er > tolerancia):
        k += 1
        xa = funcao.subs(x, xi)
        Er = abs(xi - xa)
        xi = xa
        print(xi.evalf())
    return xi.evalf()


if __name__ == '__main__':
    x = Symbol('x')
    expr = (e ** (x - 1)) / 2
    aproxini = 1.5
    toler = 10 ** -5
    itmax = 100
    funcao(expr, aproxini, toler, itmax)
    input()