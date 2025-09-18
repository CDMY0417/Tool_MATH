def calculate_expansion(power: int) -> list[int]:
    import math
    coefficients = [math.comb(power, k) for k in range(power + 1)]
    return [10**i * coefficients[i] for i in range(power + 1)]
