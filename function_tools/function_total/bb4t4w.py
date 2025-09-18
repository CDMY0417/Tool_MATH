import numpy as np
def solve_linear_system(coefficients: list[list[float]], constants: list[float]) -> list[float]:
    A = np.array(coefficients)
    b = np.array(constants)
    return np.linalg.solve(A, b).tolist()
