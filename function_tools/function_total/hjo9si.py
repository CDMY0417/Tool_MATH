def evaluate_polynomial_at_value(roots: list[int], multiplicities: list[int], leading_coeff: int, x: int) -> int:
    value = leading_coeff
    for root, multiplicity in zip(roots, multiplicities):
        value *= (x - root) ** multiplicity
    return value
