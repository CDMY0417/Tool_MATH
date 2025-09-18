def add_equations(a1: str, b1: str, total1: int, a2: str, b2: str, total2: int):
    combined_vars = set([a1, b1, a2, b2])
    return '+'.join(sorted(combined_vars)), total1 + total2
