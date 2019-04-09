# Given a square array of n x n, where n> = 5, multiply 5 consecutive digits vertically, horizontally and diagonally, returning the largest product

lista = [[2, 1, 1, 1, 1, 3],
        [1, 2, 1, 1, 3, 1],
        [1, 1, 2, 3, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 2]]

# Size

n_lins = len(lista)
n_cols = len(lista[0])

if n_lins >= 5:
    maior = lista [0] [0] * lista [0] [1] * lista [0] [2]
else:
    maior = lista [0] [0] * lista [1] [0] * lista [2] [0]

# Sweep array looking for someone greater than the greatest
# To an initial position (i0, j0) checks the possible values in row, column and 2 diagonals

for i0 in range(n_lins):
    for j0 in range(n_cols):
        for m, n in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            produto = 1
            for k in range(5):
                if 0<= i0 + m*k < n_lins and 0 <= j0 + n*k < n_cols:
                    produto *= lista[i0 + m*k] [j0 + n*k]
                else:
                    produto = maior
            if produto > maior:
                maior = produto
print('The greatest product is: ', maior)

def drawPyramid(linhas):
    draw = ''
    for i in range(linhas+1):
        linha = ''
        linha += '_'*(linhas-i)
        linha += '*'*(i*2+1)
        linha += '_'*(linhas-i)
        draw += linha + '\n'
    return draw
linhas = maior
print(drawPyramid(linhas))