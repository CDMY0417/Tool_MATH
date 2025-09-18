def divide_by_fraction(number: int, fraction: tuple) -> int:
    reciprocal = (fraction[1], fraction[0])
    return number * reciprocal[0] // reciprocal[1]
