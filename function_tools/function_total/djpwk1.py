def compute_gcd(num1: int, num2: int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
