def repeating_decimal_to_fraction(repeat: str):
    length = len(repeat)
    numerator = int(repeat)
    denominator = 10 ** length - 1
    return (numerator, denominator)
