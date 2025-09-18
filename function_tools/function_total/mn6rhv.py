def factor_out_common_term(coefficients: tuple[int]) -> tuple[tuple[int], int]:
    import math
    common_term = coefficients[0]
    for coefficient in coefficients:
        if coefficient != 0:
            common_term = math.gcd(common_term, coefficient)
    return tuple(coefficient // common_term for coefficient in coefficients), common_term
