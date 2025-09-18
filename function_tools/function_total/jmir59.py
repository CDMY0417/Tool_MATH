def prime_divisor_conditional_check(n: int, divisor: int):
    return n % divisor == 0 or (n + 1) % divisor == 0
