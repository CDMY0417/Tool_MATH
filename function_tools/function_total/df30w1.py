def multiply_matrix_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    x, y = vector[0], vector[1]
    return [a * x + b * y, c * x + d * y]
