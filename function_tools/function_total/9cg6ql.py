def list_two_digit_divisors(number: int) -> list:
    return [i for i in range(10, 100) if number % i == 0]
