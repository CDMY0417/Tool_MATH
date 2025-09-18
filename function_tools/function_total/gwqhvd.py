def multiply_by_conjugate(numerator: float, denominator_real: float, denominator_imaginary: float):
    conjugate = denominator_real - denominator_imaginary
    new_numerator = numerator * conjugate
    new_denominator = denominator_real**2 - denominator_imaginary**2
    return new_numerator, new_denominator
