def odd_multiple_of_180(value: int) -> bool:
    return value % 180 == 0 and (value // 180) % 2 != 0
