def convert_to_mixed_number(numerator: int, denominator: int):
    whole = numerator // denominator
    fractional = numerator % denominator
    return whole, fractional, denominator
