def minor_2x2(matrix: list[list[float]]) -> float:
    assert len(matrix) == 2 and all(len(row) == 2 for row in matrix)
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
