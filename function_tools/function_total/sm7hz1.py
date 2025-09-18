def complete_the_square(a: int, b: int, c: int):
    center_x = b
    center_y = c
    constant = a + b**2 + c**2
    return (center_x, center_y, constant)
