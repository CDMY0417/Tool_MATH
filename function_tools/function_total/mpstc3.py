def chinese_remainder_theorem(remainders: list[int], moduli: list[int]) -> int:
    total = 0
    prod = 1
    for mod in moduli:
        prod *= mod
    for remainder, mod in zip(remainders, moduli):
        p = prod // mod
        total += remainder * pow(p, -1, mod) * p
    return total % prod
