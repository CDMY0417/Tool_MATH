def is_divisible(number: int, divisors: list[int]) -> bool:
    for d in divisors:
        if number % d == 0:
            return True
    return False
