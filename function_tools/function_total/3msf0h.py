def repeating_decimal_to_fraction(non_repeating: str, repeating: str):
    from fractions import Fraction
    if non_repeating:
        non_repeat_value = int(non_repeating)
        non_repeat_multiplier = 10 ** len(non_repeating)
    else:
        non_repeat_value = 0
        non_repeat_multiplier = 1
    repeat_value = int(repeating)
    repeat_multiplier = 10 ** len(repeating) - 1
    repeat_factor = 10 ** len(non_repeating) if non_repeating else 1
    numerator = (non_repeat_value * repeat_multiplier + repeat_value) - non_repeat_value
    denominator = repeat_multiplier * non_repeat_multiplier
    return Fraction(numerator, denominator)
