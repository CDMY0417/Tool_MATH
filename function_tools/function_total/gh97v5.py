def probability_as_fraction(successful_ways: int, total_ways: int) -> str:
    from fractions import Fraction
    return str(Fraction(successful_ways, total_ways))
