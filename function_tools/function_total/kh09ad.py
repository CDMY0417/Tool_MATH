def distribute(multiplier: int, terms: tuple) -> tuple:
    return tuple(multiplier * term for term in terms)
