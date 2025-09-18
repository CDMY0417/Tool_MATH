def factorial_division(n: int, divisors: list[int]) -> int:
    from math import factorial
    result = factorial(n)
    for d in divisors:
        result //= factorial(d)
    return result
