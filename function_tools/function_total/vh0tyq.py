def probability_as_fraction(success_outcomes: int, total_outcomes: int):
    from fractions import Fraction
    return Fraction(success_outcomes, total_outcomes)
