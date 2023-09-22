from sympy import *

def funcao(funcao, intervalo, tolerancia):
    a = intervalo[0]
    b = intervalo[1]
    fa = funcao.subs(x, a)
    fb = funcao.subs(x, b)
    while (b - a) > 2 * tolerancia:
        m = (a + b) / 2
        fm = funcao.subs(x, m)
        if (fa * fm) < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
        print(m)
    return (a + b) / 2


if __name__ == '__main__':
    x = Symbol('x')
    expr = x/5 + 3
    interv = [-20, 10]
    toler = 10 ** -5
    print(funcao(expr, interv, toler))
    input()