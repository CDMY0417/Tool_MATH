def solve_cubic_polynomial(a: int, b: int, polynomial_coeffs: tuple):
    roots = {a, b}
    p, q, r = polynomial_coeffs
    discriminant = q**2 - 4*p*r
    if discriminant >= 0:
        roots.add((-q + discriminant**0.5) / (2*p))
        roots.add((-q - discriminant**0.5) / (2*p))
    return roots
