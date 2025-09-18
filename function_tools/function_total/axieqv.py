def is_orthogonal(a: tuple, b: tuple) -> bool:
    return sum(x * y for x, y in zip(a, b)) == 0
