def probability_of_event(favorable_outcomes: int, total_outcomes: int) -> str:
    from fractions import Fraction
    return str(Fraction(favorable_outcomes, total_outcomes))
