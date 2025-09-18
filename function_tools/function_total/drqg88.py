def matrix_2x2_linear_combination(matrix: tuple, scalar_matrix: float, scalar_identity: float):
    ((m11, m12), (m21, m22)) = matrix
    return ((scalar_matrix * m11 + scalar_identity, scalar_matrix * m12), (scalar_matrix * m21, scalar_matrix * m22 + scalar_identity))
