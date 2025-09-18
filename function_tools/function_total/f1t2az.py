def sum_modulo(numbers: list, mod: int) -> int:
    total = sum(n % mod for n in numbers)
    return total % mod
