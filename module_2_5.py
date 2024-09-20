def get_matrix(n, m, values):
    matrix = [[]]
    for i in matrix:
        while len(matrix) != n:
            matrix.append(i)
            while len(i) != m:
                i.append(values)
            else:
                break
        else:
            break

    return matrix


print(get_matrix(4, 2, 13))