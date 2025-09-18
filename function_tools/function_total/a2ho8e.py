def solve_quadratic_equation(constant_offset: int, target: int):
    discriminant = target - constant_offset
    m1 = int(discriminant**0.5)
    m2 = -m1
    return m1, m2
