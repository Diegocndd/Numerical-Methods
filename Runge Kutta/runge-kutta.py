# EDO
def edo(x, y):
    return ((x - y)/2)

# acha o valor de y para um x usando um passo de tamanho h e um valor inicial
# y0 em x0.
def rungeKutta(x0, y0, x, h):
    n = (int)((x - x0) / h) # número de iterações que serão feitas
    y = y0
    print(n)
    for i in range(1, n + 1):
        k1 = h * edo(x0, y)

        k2 = h * edo(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * edo(x0 + 0.5 * h, y + 0.75 * k2)
 
        # atualiza o valor de y
        y = y + (1.0 / 9.0)*(2*k1 + 3 * k2 + 4 * k3)

        # atualiza o valor de x
        x0 = x0 + h
    return y
 
x0 = 0
y0 = 1
x = 2
h = 0.01
print ('O valor da função y no ponto ' + str(x) + ' é', rungeKutta(x0, y, x, h))
