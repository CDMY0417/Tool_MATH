def power_of_i(n: int):
    powers = [1j, -1, -1j, 1]
    return powers[n % 4]
