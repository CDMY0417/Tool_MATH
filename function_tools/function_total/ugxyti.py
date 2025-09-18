import cmath

def roots_of_unity(n: int):
    return [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
