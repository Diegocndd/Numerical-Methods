import numpy as np

TOLERANCIA = 10**(-8)

# A = np.array([
#     [1, 1, 1],
#     [3, 7, 1],
#     [4, 5, 2]
# ])

A = np.array([
    [-40, 8, 4, 2, 1],
    [8, -30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5],
])

initial_eigenvector = np.array([1, 1, 1, 1, 1])

def potencia_regular(matriz, initial_eigenvector):
    new_eigenvalue = 0
    new_eigenvector = initial_eigenvector
    erro = 1

    while (erro > TOLERANCIA):
        old_eigenvalue = new_eigenvalue
        old_eigenvector = new_eigenvector
        # linalg.norm retorna uma das 8 normas matriciais
        old_eigenvector = old_eigenvector / np.linalg.norm(old_eigenvector)
        # dot é o produto entre duas matrizes
        new_eigenvector = np.dot(matriz, old_eigenvector)
        new_eigenvalue = np.dot(old_eigenvector, new_eigenvector)
        erro = abs((new_eigenvalue - old_eigenvalue) / new_eigenvalue)

    return new_eigenvalue, old_eigenvector

(eigenvalue, eigenvector) = potencia_regular(A, initial_eigenvector)
print('AUTOVALOR: ', eigenvalue)
print('AUTOVETOR: ', eigenvector)

# print(np.linalg.eig(A))
