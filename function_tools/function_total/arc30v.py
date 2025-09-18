def roots_of_unity(n: int) -> list:
    import cmath
    roots = [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
    return roots
