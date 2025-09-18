def expand_binomial(a: int, b: int, c: int, d: int):
    x2 = a * c
    x = a * d + b * c
    constant = b * d
    return (x2, x, constant)
