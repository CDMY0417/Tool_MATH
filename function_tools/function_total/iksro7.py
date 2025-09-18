def convert_base_to_decimal(number: int, base: int) -> int:
    decimal_value = 0
    power = 1
    while number > 0:
        decimal_value += (number % 10) * power
        number //= 10
        power *= base
    return decimal_value
