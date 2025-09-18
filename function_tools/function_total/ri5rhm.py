def find_integer_roots(coefficients: list[int], possible_roots: list[int]) -> list[int]:
    def evaluate_poly(poly, x):
        return sum(coef * (x ** i) for i, coef in enumerate(poly))
    roots = []
    for r in possible_roots:
        if evaluate_poly(coefficients, r) == 0:
            roots.append(r)
    return roots
