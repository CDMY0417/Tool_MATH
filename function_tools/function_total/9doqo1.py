def complex_product(c1: tuple[float, float], c2: tuple[float, float]) -> tuple[float, float]:
    a, b = c1
    c, d = c2
    return (a*c - b*d, a*d + b*c)
