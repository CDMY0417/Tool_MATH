def factor_quadratic(a: int, b: int, c: int):
    # Assuming the quadratic can be factored into integers
    for i in range(-abs(c), abs(c) + 1):
        if i != 0 and c % i == 0:
            j = c // i
            if a * i + b + j == 0:
                return (1, i), (1, j)
    return None
