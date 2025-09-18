def probability_common_fraction(successful_outcomes: int, total_outcomes: int) -> str:
    from fractions import Fraction
    return str(Fraction(successful_outcomes, total_outcomes))
