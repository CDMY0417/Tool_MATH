def linear_congruence_solutions(a: int, b: int, m: int, limit: int):
    a_mod = a % m
    b_mod = b % m
    sol = (b_mod * pow(a_mod, -1, m)) % m
    solutions = []
    while sol <= limit:
        if sol > 0:
            solutions.append(sol)
        sol += m
    return solutions
