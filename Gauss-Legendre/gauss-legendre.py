import numpy as np

def function(x):
    return 10 - (2 * np.sin(8 * x) * np.exp(-x ** 2.5))
    # return np.exp(-x ** 2)

# intervalo [a,b] para [-1,1]
def x_s(a, b, s):
    return ((b + a) / 2.0) + (((b - a) / 2.0) * s)

def gauss_legendre(a, b, pontos):
    if pontos == 2:
        w1 = 1.0
        w2 = 1.0

        a1 = -np.sqrt(1.0 / 3.0)
        a2 = np.sqrt(1.0 / 3.0)

        return ((b - a) / 2.0) * (((function(x_s(a, b, a1)) * w1) + (function(x_s(a, b, a2)) * w2)))
    elif pontos == 3:
        w1 = 5.0 / 9.0
        w2 = 8.0 / 9.0
        w3 = 5.0 / 9.0

        a1 = -np.sqrt(3.0 / 5.0)
        a2 = 0.0
        a3 = np.sqrt(3.0 / 5.0)

        return ((b - a) / 2.0) * (((function(x_s(a, b, a1)) * w1) + (function(x_s(a, b, a2)) * w2) + (function(x_s(a, b, a3)) * w3)))
    elif pontos == 4:
        w1 = 0.652145
        w2 = 0.652145
        w3 = 0.347855
        w4 = 0.347855

        a1 = -np.sqrt((3.0 / 7.0) - ((2.0*np.sqrt(6.0 / 5.0)) / 7.0))
        a2 = np.sqrt((3.0 / 7.0) - ((2.0*np.sqrt(6.0 / 5.0)) / 7.0))
        a3 = -np.sqrt((3.0 / 7.0) - ((2.0*np.sqrt(6.0 / 5.0)) / 7.0))
        a4 = np.sqrt((3.0 / 7.0) - ((2.0*np.sqrt(6.0 / 5.0)) / 7.0))
        
        return ((b - a) / 2.0) * (((function(x_s(a, b, a1)) * w1) + (function(x_s(a, b, a2)) * w2) + (function(x_s(a, b, a3)) * w3) + (function(x_s(a, b, a4)) * w4)))

a = 0
b = np.pi
pontos = 2

iN = gauss_legendre(a, b, pontos)

N = 1
erro = 1

precisao = 10**(-6)

while erro > precisao:
    N *= 2
    # delta
    d = (b - a) / N

    iV = iN
    iN = 0.0

    for i in range(N):
        a_atual = a + (i * d)
        b_atual = a_atual + d
        iN += gauss_legendre(a_atual, b_atual, pontos)
    
    erro = abs((iN - iV) / iV)

print('Integral: ', iN)