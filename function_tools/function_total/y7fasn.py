def matrix_multiply(matrix1: tuple[tuple[float, float], tuple[float, float]], matrix2: tuple[tuple[float, float], tuple[float, float]]) -> tuple[tuple[float, float], tuple[float, float]]:
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return ((a*e + b*g, a*f + b*h), (c*e + d*g, c*f + d*h))
