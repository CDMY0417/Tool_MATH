def ends_with_digits_divisible_by(number: int, divisor: int) -> bool:
    return int(str(number)[-2:]) % divisor == 0
