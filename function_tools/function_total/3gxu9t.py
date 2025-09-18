def convert_repeating_decimal_to_fraction(decimal_str: str, repeating_part: str):
    length_of_repeating = len(repeating_part)
    multiplier = 10 ** length_of_repeating
    non_repeating_decimal = decimal_str + repeating_part
    repeating_value = int(non_repeating_decimal) - int(decimal_str)
    denominator = multiplier - 1
    return (repeating_value, denominator)
