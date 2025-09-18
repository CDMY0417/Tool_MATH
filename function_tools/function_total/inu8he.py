def polynomial_subtraction(poly1: dict[int, float], poly2: dict[int, float]) -> dict[int, float]:
    result = poly1.copy()
    for degree, coef in poly2.items():
        if degree in result:
            result[degree] -= coef
        else:
            result[degree] = -coef
    return {deg: coef for deg, coef in sorted(result.items(), reverse=True) if coef != 0}
