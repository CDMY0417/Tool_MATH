def is_matrix_zero(matrix: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    return all(element == 0 for row in matrix for element in row)
