def is_divisible_by_4(tens: int, units: int) -> bool:
    number = tens * 10 + units
    return number % 4 == 0
