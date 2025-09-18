def cancel_common_factors(numerator: tuple[int, ...], denominator: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    num_set = set(numerator)
    denom_set = set(denominator)
    common = num_set.intersection(denom_set)
    for factor in common:
        numerator = tuple(x for x in numerator if x != factor)
        denominator = tuple(x for x in denominator if x != factor)
    return numerator, denominator
