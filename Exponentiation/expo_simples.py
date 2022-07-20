from cmath import isnan
import math

def f(x):
    return 1 / math.sqrt(4 - x**2)
    # return math.cos(x)
    # return x**2 + 5
    # return 1.0 / math.sqrt(x)

def x_s(ini, fim, s):
    return ((ini + fim) / 2.0) + (((fim - ini) / 2.0) * math.tanh(s))

def s_barra(ini, fim, s):
    return ((fim + ini) / 2.0) + (((fim - ini) / 2.0) * s)

def f_barra(ini, fim, s):
    return f(x_s(ini, fim, s)) * ((fim - ini) / 2.0) * (1.0 / math.pow(math.cosh(s), 2))

def gaussLegendreExpSimples(ini, fim, iniC, fimC, qtdPontos):
    resultado = 0.0
    w1 = w2 = w3 = None
    s1 = s2 = s3 = None

    if qtdPontos == 2:
        w1 = w2 = 1.0
        s1 = -1.0 / math.sqrt(3.0)
        s2 = +1.0 / math.sqrt(3.0)

        return ((fimC - iniC) / 2.0) * ((f_barra(ini, fim, s_barra(iniC, fimC, s1)) * w1) + (f_barra(ini, fim, s_barra(iniC, fimC, s2)) * w2))
    elif qtdPontos == 3:
        w1 = w3 = 5.0 / 9.0
        w2 = 8.0 / 9.0

        s1 = -math.sqrt(3.0 / 5.0)
        s2 = 0.0
        s3 = +math.sqrt(3.0 / 5.0)

        return ((fimC - iniC) / 2.0) * ((f_barra(ini, fim, s_barra(iniC, fimC, s1)) * w1) + (f_barra(ini, fim, s_barra(iniC, fimC, s2)) * w2) + (f_barra(ini, fim, s_barra(iniC, fimC, s3)) * w3))

def GaussLegendreParticoesExpSImples(ini, fim, iniC, fimC, qtdPontos, eps):
    integralNova = 1e10
    integralVelha = 0.0
    N = 1 # quantidade de intervalos

    while (abs((integralNova - integralVelha) / integralNova) > eps):
        integralVelha = integralNova
        deltaX = (fimC - iniC) / N # tamanho de cada intervalo
        integralNova = 0.0

        for i in range(0, N):
            xIn = iniC + (i * deltaX)
            xFim = xIn + deltaX
            integralNova += gaussLegendreExpSimples(ini, fim, xIn, xFim, qtdPontos)
        N *= 2

    return integralNova

eIni = 0
eFim = 2
qtdPontos = 2
cInicial = 5
eps = 10**(-6)

resultNovo = 1e100
resultVelho = 0.0
passo = 0.1

c = cInicial

while (abs((resultNovo - resultVelho) / resultNovo) > eps):
    resultVelho = resultNovo
    resultNovo = GaussLegendreParticoesExpSImples(eIni, eFim, -c, c, qtdPontos, eps)

    c += passo

    if (isnan(resultNovo) or resultNovo == 1e100):
        # c = cInicial
        # passo /= 10
        # resultNovo = 1e100
        break

print(resultNovo)
