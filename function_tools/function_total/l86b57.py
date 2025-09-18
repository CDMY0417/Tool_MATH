def scale_matrix(matrix: list[list[float]], factor: float):
    return [[factor * entry for entry in row] for row in matrix]
