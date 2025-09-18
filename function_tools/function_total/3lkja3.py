def probability_as_reduced_fraction(numerator: int, total_space: int):
    from math import gcd
    denominator = 2 ** total_space
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)
