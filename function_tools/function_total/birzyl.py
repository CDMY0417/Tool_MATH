def expand_binomial_product(a: int, b: int, c: int, d: int) -> tuple:
    return (a * c, a * d + b * c, b * d)
