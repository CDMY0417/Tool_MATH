def find_vertical_asymptotes(numerator: tuple, denominator: tuple):
    num_factors = set(numerator)
    den_factors = set(denominator)
    vertical_asymptotes = den_factors - num_factors
    return list(vertical_asymptotes)
