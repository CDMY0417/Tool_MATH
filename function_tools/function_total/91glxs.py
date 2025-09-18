def generate_divisors(factors: list[int]) -> set:
    divisors = {1}
    for f in factors:
        divisors.update({d * f for d in divisors})
    return divisors
