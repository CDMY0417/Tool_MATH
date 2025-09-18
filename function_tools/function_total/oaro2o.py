def odd_divisors(num: int):
    divisors = [i for i in range(1, abs(num) + 1, 2) if num % i == 0]
    return divisors
