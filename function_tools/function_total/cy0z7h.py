def solve_exponential_equation(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    # Assume a and d can be expressed as the power of the same base
    # Simplify ax + c = ex + f
    return (f - c) / (b - e)
