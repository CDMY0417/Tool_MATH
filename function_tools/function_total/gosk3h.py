def convert_to_scientific_notation_base(number: int, base: float) -> int:
    exponent = 0
    while base * (10 ** exponent) < number:
        exponent += 1
    return exponent - 1
