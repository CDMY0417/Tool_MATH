def triangle_area_by_shoelace(b_x: int, b_y: int, p: int, q: int) -> float:
    return 0.5 * abs(b_x * q - b_y * p)
