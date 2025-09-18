def convert_base_to_decimal(number: str, base: int) -> int:
    decimal_value = 0
    exponent = len(number) - 1
    for digit in number:
        decimal_value += int(digit) * (base ** exponent)
        exponent -= 1
    return decimal_value
