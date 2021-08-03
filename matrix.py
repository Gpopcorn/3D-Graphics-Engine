def multiply_matrix(a, b):
    rowsA = len(a)
    colsA = len(a[0])
    rowsB = len(b)
    colsB = len(b[0])

    c = [[0 for row in range(colsB)] for col in range(rowsA)]

    for x in range(rowsA):
        for y in range(colsB):
            for z in range(colsA):
                c[x][y] += a[x][z] * b[z][y]

    return c
