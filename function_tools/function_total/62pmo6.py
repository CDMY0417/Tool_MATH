def combine_fractions(numerators: list[int], denominator: int) -> str:
    combined_numerator = sum(numerators)
    return f'{combined_numerator}/{denominator}'
