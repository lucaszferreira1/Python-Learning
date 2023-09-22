from sympy import *
from math import e

def funcao(funcao, xi, tolerancia, kmax):
    k = 0
    f = funcao.subs(x, xi)
    funcaoder = diff(funcao)
    Dr = tolerancia + 1
    while (k <= kmax) and (Dr > tolerancia):
        k += 1
        xa = xi - (f / (funcaoder.subs(x, xi)))
        Dr = abs(xa - xi)
        xi = xa
        f = funcao.subs(x, xi)
        print(xi.evalf())
    return xi.evalf()


if __name__ == '__main__':
    x = Symbol('x')
    expr = (x ** 2) - 3
    aproxini = 5
    toler = 10 ** -5
    itmax = 100
    funcao(expr, aproxini, toler, itmax)
    input()