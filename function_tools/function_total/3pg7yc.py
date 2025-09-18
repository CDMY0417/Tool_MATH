def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    s = int(x**0.5)
    return s * s == x
