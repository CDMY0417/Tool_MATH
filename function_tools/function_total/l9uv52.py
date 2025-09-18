def is_valid_triangle(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a
