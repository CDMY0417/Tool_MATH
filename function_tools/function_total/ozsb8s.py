def simplify_radical(factor_dict: dict[int, int]) -> tuple[int, int]:
    outside = 1
    inside = 1
    for factor, exponent in factor_dict.items():
        outside *= factor ** (exponent // 2)
        if exponent % 2 == 1:
            inside *= factor
    return outside, inside
