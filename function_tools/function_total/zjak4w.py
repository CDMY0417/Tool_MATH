def solve_linear_system(A: list[list[float]], b: list[float]) -> tuple:
    from numpy import linalg
    import numpy as np
    A_matrix = np.array(A)
    b_vector = np.array(b)
    solution = linalg.solve(A_matrix, b_vector)
    return tuple(solution)
