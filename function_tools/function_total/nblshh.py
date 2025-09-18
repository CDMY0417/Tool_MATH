from numpy.linalg import solve
import numpy as np
def solve_linear_equations_3x3(equation_matrix: list[list[float]], result_vector: list[float]) -> list[float]:
    A = np.array(equation_matrix)
    B = np.array(result_vector)
    return solve(A, B).tolist()
