def triangle_inequality_constraints(sides: list[float]) -> list[bool]:
    a, b, c = sides
    return [(a + b > c), (a + c > b), (b + c > a)]
