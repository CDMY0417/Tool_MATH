def convert_to_decimal(number: int, base: int) -> int:
    decimal_value = 0
    power = 0
    while number > 0:
        decimal_value += (number % 10) * (base ** power)
        number //= 10
        power += 1
    return decimal_value
