def multiply_polynomials(polynomials: list[list[float]]):
    from numpy.polynomial import Polynomial
    result = Polynomial([1])
    for poly in polynomials:
        result *= Polynomial(poly)
    return result
