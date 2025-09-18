def hypotenuse_to_side_length(hypotenuse: float, other_side: float) -> float:
    side_length = (hypotenuse**2 - other_side**2) ** 0.5
    return side_length
