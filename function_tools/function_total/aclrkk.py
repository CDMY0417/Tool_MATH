def calculate_weighted_vector(t: float, u: float, a: tuple, b: tuple) -> tuple:
    px = t * a[0] + u * b[0]
    py = t * a[1] + u * b[1]
    return (px, py)
