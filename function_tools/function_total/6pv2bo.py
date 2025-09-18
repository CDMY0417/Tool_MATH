def is_isosceles_right_triangle(side_length1: float, side_length2: float, hypotenuse_length: float) -> bool:
    return abs((side_length1**2 + side_length2**2) - hypotenuse_length**2) < 1e-9
