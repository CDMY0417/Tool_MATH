def power_of_i(exponent: int) -> complex:
    powers = [1, 1j, -1, -1j]
    return powers[exponent % 4]
