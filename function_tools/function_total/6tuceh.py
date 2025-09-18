def law_of_cosines(side1: float, side2: float, cos_angle: float) -> float:
    return (side1**2 + side2**2 - 2 * side1 * side2 * cos_angle) ** 0.5
