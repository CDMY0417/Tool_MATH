def units_digit_of_product(a: int, b: int, c: int) -> int:
    result = (a % 10) * (b % 10) * (c % 10)
    return result % 10
