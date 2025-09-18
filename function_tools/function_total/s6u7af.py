def remove_divisors(number: int, numbers_set: set[int]) -> set[int]:
    divisors = {i for i in numbers_set if number % i == 0}
    return numbers_set - divisors
