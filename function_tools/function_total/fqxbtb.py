def matrix_add(matrix1: tuple[tuple[int, int], tuple[int, int]], matrix2: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((matrix1[0][0] + matrix2[0][0], matrix1[0][1] + matrix2[0][1]),
            (matrix1[1][0] + matrix2[1][0], matrix1[1][1] + matrix2[1][1]))
