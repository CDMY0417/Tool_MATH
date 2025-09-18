def simplify_exponent(base: float, numerator_exponent: float, denominator_exponent: float) -> float:
    return base ** (numerator_exponent - denominator_exponent)
