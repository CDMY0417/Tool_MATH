def convert_base_to_decimal(number: int, base: int) -> int:
    digits = list(map(int, str(number)))[::-1]
    decimal_value = sum(d * (base ** i) for i, d in enumerate(digits))
    return decimal_value
