import scipy.optimize as sp

def f(x):
    return x[0]**2 + x[1]**2

def der(x):
    return [2*x[0], 2*x[1]]

if __name__ == '__main__':
    xi = [2, 5]
    result = sp.minimize(f, xi, method='BFGS', jac=der)
    print(result['x'])