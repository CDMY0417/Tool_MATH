def solve_linear_diophantine(a: int, b: int, c: int):
    from math import gcd
    if c % gcd(a, b) != 0:
        return None
    # Extended Euclidean algorithm
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)
    g, x, y = extended_gcd(a, b)
    x *= c // g
    y *= c // g
    return (x, y)
