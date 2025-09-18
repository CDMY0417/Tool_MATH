def simplify_radical(n: int):
    factor = 1
    while factor * factor * 4 <= n:
        factor *= 2
    return (factor, int(n / (factor * factor)))
