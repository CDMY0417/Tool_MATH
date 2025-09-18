def constant_term_of_polynomial(roots: list[int]) -> int:
    constant_term = 1
    for root in roots:
        constant_term *= root
    return constant_term
