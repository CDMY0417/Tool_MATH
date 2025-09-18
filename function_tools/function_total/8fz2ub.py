def is_geometric_sequence(a: int, b: int, c: int) -> bool:
    if b == 0 or a == 0:
        return False
    return (b / a) == (c / b)
