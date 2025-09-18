def subtract_matrix_columns(matrix: list[list[float]], col1: int, col2: int) -> list[list[float]]:
    result = [row[:] for row in matrix]
    for row in result:
        row[col1] -= row[col2]
    return result
