def compose_linear_functions(a: int, b: int, c: int, d: int) -> tuple:
    new_a = a * c
    new_b = a * d + b
    return (new_a, new_b)
