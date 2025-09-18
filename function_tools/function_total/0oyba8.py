def evaluate_plane_equation(coeff: tuple, point: tuple) -> float:
    A, B, C, D = coeff
    x, y, z = point
    return A*x + B*y + C*z + D
