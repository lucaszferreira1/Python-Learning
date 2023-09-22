from sympy import *

def funcao(funcao, aproximacoes, tolerancia, et, kmax):
    x0 = aproximacoes[0]
    x1 = aproximacoes[1]
    k = 0
    Dr = tolerancia + 1
    f0 = funcao.subs(x, x0)
    f1 = funcao.subs(x, x1)
    while (k <= kmax) and (abs(f1) > et) and (Dr > tolerancia):
        k += 1
        d = (f1 - f0) / (x1 - x0)
        xa = x1 - (f1 / d)
        Dr = abs(xa - x1)
        x0 = x1
        f0 = f1
        x1 = xa
        f1 = funcao.subs(x, x1)
        print(xa.evalf())
    return xa.evalf()


if __name__ == '__main__':
    x = Symbol('x')
    expr = x**3 - 2*x**2 - 5
    aproxini = [2, 4]
    toler = 10 ** -5
    etol = toler
    itmax = 20
    funcao(expr, aproxini, toler, etol, itmax)
    input()