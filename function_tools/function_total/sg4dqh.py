def generate_composite_plane(plane1: tuple, plane2: tuple, coefficient1: int, coefficient2: int) -> tuple:
    return tuple(coefficient1 * p1 + coefficient2 * p2 for p1, p2 in zip(plane1, plane2))
