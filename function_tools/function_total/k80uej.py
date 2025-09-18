def distribute(factor: int, terms: tuple) -> tuple:
    return tuple(factor * term for term in terms)
