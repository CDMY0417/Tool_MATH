def sum_equations(equations: list[list[float]]) -> list[float]:
    return [sum(terms) for terms in zip(*equations)]
