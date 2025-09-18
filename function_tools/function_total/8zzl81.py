def fraction_greater_than_or_equal(a: int, b: int, c: int, threshold: float) -> bool:
    if b >= c:
        return False
    return (a + b) / (c - b) >= threshold
