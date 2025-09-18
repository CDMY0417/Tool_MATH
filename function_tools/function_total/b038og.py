def units_digit_of_power(base: int, exponent: int) -> int:
    return (base % 10) ** (exponent % 4 + 4) % 10
