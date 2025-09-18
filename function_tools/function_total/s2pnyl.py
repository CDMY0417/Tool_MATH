def calculate_lcm_from_exponents(prime_exponents: dict[int, int]) -> int:
    lcm = 1
    for prime, exponent in prime_exponents.items():
        lcm *= prime ** exponent
    return lcm
