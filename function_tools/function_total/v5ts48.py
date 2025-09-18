def compute_probability(successful_outcomes: int, total_outcomes: int) -> str:
    from fractions import Fraction
    return str(Fraction(successful_outcomes, total_outcomes))
