def multiply_term_factors(factors1: dict[int, int], factors2: dict[int, int]) -> dict[int, int]:
    result = factors1.copy()
    for prime, exponent in factors2.items():
        if prime in result:
            result[prime] += exponent
        else:
            result[prime] = exponent
    return result
