def find_integer_in_range(x: float) -> int:
    a = int(x)
    return a if a < x < a + 1 else None
