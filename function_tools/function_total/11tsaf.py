def solve_quadratic(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    sqrt_disc = discriminant**0.5
    sol1 = (-b + sqrt_disc) / (2*a)
    sol2 = (-b - sqrt_disc) / (2*a)
    return sol1, sol2
