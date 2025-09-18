def is_divisible_by_8(number: int) -> bool:
    return int(str(number)[-3:]) % 8 == 0
