def find_polynomial_given_points(evaluations: list[float], points: list[float]) -> list[float]:
    from sympy import symbols, Eq, solve
    n = len(points)
    a = symbols(f'a0:{n}')
    equations = [Eq(sum(a[i] * (points[j] ** i) for i in range(n)), evaluations[j]) for j in range(n)]
    solution = solve(equations, a)
    return [solution[ai] for ai in a]
