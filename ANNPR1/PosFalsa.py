from sympy import *

def funcao(funcao, intervalo, tolerancia, et):
    a = intervalo[0]
    b = intervalo[1]
    fa = funcao.subs(x, a)
    fb = funcao.subs(x, b)
    fm = et + 1
    while (abs(fm) > et) and (b - a) > (2 * tolerancia):
        d = (fb - fa) / (b - a)
        m = b - (fb / d)
        fm = funcao.subs(x, m)
        if (fa * fm) < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
        print(m.evalf())
    return m.evalf() if abs(fm) <= et else ((a * fb - b * fa) / (fb - fa)).evalf()

if __name__ == '__main__':
    x = Symbol('x')
    expr = (x ** 2) - 3
    interv = [0, 10]
    toler = 10 ** -1
    etol = toler
    print(funcao(expr, interv, toler, etol))
    input()