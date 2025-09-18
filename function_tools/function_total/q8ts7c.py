def distribute_terms(exp1: tuple[float, float], exp2: tuple[float, float, float]):
    a1, a2 = exp1
    b1, b2, b3 = exp2
    distribution = (a1 * b1, a1 * b2, a1 * b3, a2 * b1, a2 * b2, a2 * b3)
    expanded = (distribution[0], distribution[1], distribution[3], distribution[4], distribution[5])
    return expanded
