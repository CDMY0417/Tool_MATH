def product_of_fractions(numerators: list[float], denominators: list[float]) -> float:
    num, denom = 1, 1
    for n in numerators:
        num *= n
    for d in denominators:
        denom *= d
    return num / denom
