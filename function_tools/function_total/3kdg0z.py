def convert_from_decimal(decimal_number: int, base: int) -> int:
    result = 0
    power = 1
    while decimal_number > 0:
        result += (decimal_number % base) * power
        decimal_number //= base
        power *= 10
    return result
