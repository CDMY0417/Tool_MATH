def count_congruent_solutions_below_limit(a: int, m: int, limit: int) -> int:
    smallest_solution = a % m if a % m != 0 else m
    if smallest_solution >= limit:
        return 0
    return (limit - smallest_solution) // m + 1
