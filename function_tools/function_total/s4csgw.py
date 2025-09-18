def add_fractions(fractions: list[str]):
    from fractions import Fraction
    total = sum(Fraction(f) for f in fractions)
    return total.limit_denominator()
