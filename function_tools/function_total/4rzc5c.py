def convert_improper_to_mixed_number(numerator: int, denominator: int):
    whole = numerator // denominator
    remainder = numerator % denominator
    return whole, remainder, denominator
