from sympy import *
import numpy as np


def funcao(funcao, xi, jacobiana, tolerancia, kmax):
    k = 0
    Fx = funcao.subs({x:xi[0], y:xi[1]})
    Fx = np.array(Fx).astype(np.float64)
    Dr = np.linalg.norm(Fx, ord=2)
    while abs(Dr) > tolerancia and k <= kmax:
        k += 1 # k = k + 1
        J = jacobiana.subs({x:xi[0], y:xi[1]})
        J = np.array(J).astype(np.float64)
        s = np.linalg.solve(J, -Fx) # J(x)s = -Fx
        xi[0] += s[0][0]
        xi[1] += s[1][0] # x = x + s
        Fx = funcao.subs({x:xi[0], y:xi[1]}) # Fx = F(x)
        Fx = np.array(Fx).astype(np.float64)
        Dr = np.linalg.norm(Fx, ord=2) # Dr = ||s||
        print(xi)
    return xi


if __name__ == '__main__':
    x, y = symbols('x y')
    expr1 = (x**2) + 4*(y**2) - 4
    expr2 = (x**2) - 2*x - 2*y + 1
    aproxini = [1, 0]
    kmaximo = 100
    expressoes = Matrix([expr1, expr2])
    toler = 10 ** -8
    jacob = Matrix([[diff(expr1, x), diff(expr1, y)], [diff(expr2, x), diff(expr2, y)]])
    print(aproxini)
    funcao(expressoes, aproxini, jacob, toler, kmaximo)
    aproxini = [0, 1]
    print(aproxini)
    funcao(expressoes, aproxini, jacob, toler, kmaximo)
    input()