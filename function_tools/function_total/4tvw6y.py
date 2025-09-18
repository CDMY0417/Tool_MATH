def modular_exponentiation_equivalence(a: int, b: int, power: int, mod: int) -> bool:
    remainder_a = pow(a, power, mod)
    remainder_b = pow(b, power, mod)
    return remainder_a == remainder_b
