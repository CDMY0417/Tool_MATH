def polynomial_addition(poly1: list[int], poly2: list[int]) -> list[int]:
    if len(poly1) < len(poly2):
        poly1, poly2 = poly2, poly1
    result = poly1[:]
    for i in range(1, len(poly2) + 1):
        result[-i] += poly2[-i]
    return result
