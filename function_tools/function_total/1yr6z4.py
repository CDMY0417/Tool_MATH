def has_exactly_four_factors(n: int) -> bool:
    num_factors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                num_factors += 1
            else:
                num_factors += 2
        if num_factors > 4:
            return False
    return num_factors == 4
