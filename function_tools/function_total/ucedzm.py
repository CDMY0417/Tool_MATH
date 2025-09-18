def limit_polynomial_degree(criterion_value: int, limit_value: int) -> int:
    degree = 0
    while (criterion_value ** degree) < limit_value:
        degree += 1
    return degree - 1
