def least_common_multiple(a: int, b: int) -> int:
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
