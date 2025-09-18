def gcd(x: int, y: int):
    while y != 0:
        (x, y) = (y, x % y)
    return x
