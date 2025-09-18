def power_of_i(n: int):
    powers = [1, 1j, -1, -1j]
    return powers[n % 4]
