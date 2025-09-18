def triangle_inequality_check(a: int, b: int, c: int) -> bool:
    return a + b > c and b + c > a and a + c > b
