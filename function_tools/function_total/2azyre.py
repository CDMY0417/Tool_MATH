def sum_of_odd_divisors(factor_dict: dict[int, int]) -> int:
    result = 1
    for prime, power in factor_dict.items():
        if prime % 2 != 0:  # check if the prime is odd
            result *= sum(prime ** i for i in range(power + 1))
    return result
