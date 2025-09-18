def simplify_fraction(num: int, den: int):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    greatest_common_divisor = gcd(num, den)
    return num // greatest_common_divisor, den // greatest_common_divisor
