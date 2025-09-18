def mult_bound_fraction(numerator: int, denominator: int, factor: int):
    lower = (numerator * factor) // denominator
    upper = (numerator * factor) // denominator + 1
    return lower + 1 if lower * denominator == numerator * factor else lower, upper
