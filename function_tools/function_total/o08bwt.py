def scalar_multiply_matrix(scalar: int, matrix: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((scalar * matrix[0][0], scalar * matrix[0][1]), (scalar * matrix[1][0], scalar * matrix[1][1]))
