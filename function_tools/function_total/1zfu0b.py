def find_opposite_side(adjacent: float, hypotenuse: float) -> float:
    opposite = (hypotenuse**2 - adjacent**2)**0.5
    return opposite
