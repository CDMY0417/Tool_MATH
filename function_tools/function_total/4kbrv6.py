def triangle_inequality(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a
