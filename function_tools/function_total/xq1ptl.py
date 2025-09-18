def solutions_quadratic(b: int, c: int) -> set:
    solutions = set()
    discriminant = b**2 + 4*c
    if discriminant >= 0:
        sqrt_discriminant = int(discriminant**0.5)
        if sqrt_discriminant**2 == discriminant:
            solutions.add((-b + sqrt_discriminant) // 2)
            solutions.add((-b - sqrt_discriminant) // 2)
    return solutions
