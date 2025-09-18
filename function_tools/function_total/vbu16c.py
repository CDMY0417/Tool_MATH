def combine_fractions(whole_number: int, numerator: int, denominator: int) -> str:
    total_numerator = whole_number * denominator + numerator
    return f'{total_numerator}/{denominator}'
