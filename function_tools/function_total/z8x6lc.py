def calculate_ratio(area1: int, area2: int) -> str:
    from fractions import Fraction
    return str(Fraction(area1, area2))
