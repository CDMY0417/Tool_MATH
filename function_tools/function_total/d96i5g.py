def factor_quadratic(b: int, c: int):
    for i in range(-abs(c), abs(c) + 1):
        if i != 0 and c % i == 0:
            j = c // i
            if i + j == b:
                return (i, j)
    return None
