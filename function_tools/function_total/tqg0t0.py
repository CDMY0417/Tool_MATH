def simplify_fraction(numerator_factors: list[int], denominator_factors: list[int]):
    i, j = 0, 0
    while i < len(numerator_factors) and j < len(denominator_factors):
        if numerator_factors[i] == denominator_factors[j]:
            i += 1
            j += 1
        elif numerator_factors[i] < denominator_factors[j]:
            i += 1
        else:
            j += 1
    simplified_numerator = numerator_factors[i:]
    simplified_denominator = denominator_factors[j:]
    return simplified_numerator, simplified_denominator
