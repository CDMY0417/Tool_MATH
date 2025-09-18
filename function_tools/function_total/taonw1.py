def is_divisible_by_11(digits: list[int]) -> bool:
    return sum(digits[0::2]) % 11 == sum(digits[1::2]) % 11
