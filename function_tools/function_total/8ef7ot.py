def vector_combination(coef1: float, vec1: tuple, coef2: float, vec2: tuple) -> tuple:
    return (coef1 * vec1[0] + coef2 * vec2[0], coef1 * vec1[1] + coef2 * vec2[1])
