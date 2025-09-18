def multiply_congruence(coeff: int, constant: int, multiplier: int, modulus: int):
    new_coeff = (coeff * multiplier) % modulus
    new_constant = (constant * multiplier) % modulus
    return new_coeff, new_constant
