def law_of_cosines(side_a: float, side_b: float, side_c: float) -> float:
    cos_theta = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
    return cos_theta
