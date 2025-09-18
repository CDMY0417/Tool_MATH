def is_right_triangle(a: int, b: int, c: int) -> bool:
    return a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a
