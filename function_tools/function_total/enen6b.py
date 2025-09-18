def combine_polynomials(poly1: tuple, poly2: tuple):
    max_len = max(len(poly1), len(poly2))
    poly1 = (0,) * (max_len - len(poly1)) + poly1
    poly2 = (0,) * (max_len - len(poly2)) + poly2
    return tuple(x + y for x, y in zip(poly1, poly2))
