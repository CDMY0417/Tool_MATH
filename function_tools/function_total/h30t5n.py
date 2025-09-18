def integer_solutions_product_equals(n: int) -> list:
    solutions = []
    for i in range(1, int(abs(n)**0.5) + 1):
        if n % i == 0:
            solutions.append((i, n // i))
            solutions.append((-i, -n // i))
    return solutions
