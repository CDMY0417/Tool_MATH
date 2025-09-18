def convert_repeating_decimal_to_fraction(x: float, repeat_length: int):
    multiplier = 10 ** repeat_length
    non_repeating_part = int(x * multiplier)
    fraction_numerator = non_repeating_part - int(x)
    fraction_denominator = multiplier - 1
    return fraction_numerator, fraction_denominator
