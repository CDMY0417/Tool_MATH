def rationalize_denominator(numerator: float, denominator: float):
    from math import sqrt
    # Multiply numerator and denominator by the square root of the denominator squared
    new_numerator = numerator * sqrt(denominator)
    new_denominator = denominator * sqrt(denominator)
    return new_numerator, new_denominator
