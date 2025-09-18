def expand_2x2_determinant(matrix: list[list[float]]) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
