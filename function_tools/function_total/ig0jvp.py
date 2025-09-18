def convert_fraction(numerator: int, denominator: int, new_denominator: int) -> int:
    return numerator * (new_denominator // denominator)
