import math

def func(x):
    return 10 - (2 * math.sin(8 * x) * math.exp(-x ** 2.5))
    # return math.exp(x ** 1.5)

def newtonCotes(a, b, precisao, formula):
    f = []
    iV = 0
    iN = 0
    cont = 0
    n = 10
    prec = 1
    while prec > (precisao):
        cont = cont + 1
        iN = 0
        h1 = (b-a)/n
        for i in range(n):
            f.append(formula(a + i*h1, a + (i+1)*h1))
            iN = iN + f[i]
        prec = abs(iN - iV)
        n = n + 1
        iV = iN
        f.clear()

    print('Integral =', iN)
    print('Numero de iterações =', cont)

def loopFechada(xi, xf, num, values, h): # num é o número de pontos interpolados
    h = ((xf - xi)/(num-1))
    for i in range(num):
        x = (xi + (i*h))
        values.append(func(x))
    return (h, values)

def loopAberta(xi, xf, num, values, h): # preencher o array com os valores da função
    h = ((xf - xi)/(num-1))
    for i in range(1, num-1):
        x = (xi + (i*h))
        values[i-1] = func(x)
    return (h, values)

def form_fechada(xi, xf):
    values = [] # array que contém os valores da função
    h = 0
    (h, values) = loopFechada(xi, xf, 5, values, h)
    integ = (2*h/45) * (7*values[0] + 32*values[1] + 12*values[2] + 32*values[3] + 7*values[4])
    return integ

def form_aberta(xi, xf):
    values = [0, 0, 0, 0, 0, 0, 0]
    h = 0
    (h, values) = loopAberta(xi, xf, 7, values, h)
    integ = (3*h/10) * ((-11*values[0]) + 74*values[1] - 84*values[2] + 30*values[3] + 11*values[4])
    return integ

precisao = 10**(-6)
a = 0
b = math.pi

print('Fórmula fechada')
newtonCotes(a, b, precisao, form_fechada)

print('\nFórmula aberta')
newtonCotes(a, b, precisao, form_aberta)
