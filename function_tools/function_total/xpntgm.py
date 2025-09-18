def simplify_fraction(numerator: int, denominator: int) -> tuple:
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)
