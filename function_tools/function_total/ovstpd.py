def law_of_cosines(side_a: float, side_b: float, side_c: float) -> float:
    return (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
