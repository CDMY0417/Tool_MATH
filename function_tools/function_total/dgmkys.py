def calculate_constant(polynomial_value: float, x_value: int, root1: int, root2: int, root3: int) -> float:
    return polynomial_value / ((x_value + root1) * (x_value + root2) * (x_value + root3))
