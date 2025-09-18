def complex_exponentiation(a: float, b: float, n: int):
    from cmath import polar, rect
    r, angle = polar(complex(a, b))
    return rect(r**n, angle*n)
