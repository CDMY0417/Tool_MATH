def is_square_root_positive_integer(x: int, offset: int) -> bool:
    n = (x + offset) ** 0.5
    return n.is_integer() and n > 0
