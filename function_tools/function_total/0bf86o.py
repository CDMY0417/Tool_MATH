def add_scaled_matrices(a: float, matrix1: list[list[float]], b: float, matrix2: list[list[float]]) -> list[list[float]]:
    return [[a * matrix1[i][j] + b * matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
