def arctan_sum_of_complements(r1: float, r2: float) -> float:
    from math import atan
    alpha = atan(r1)
    beta = atan(r2)
    return alpha + beta
