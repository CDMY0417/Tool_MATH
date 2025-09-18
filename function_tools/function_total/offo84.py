def bezouts_identity_solution(a: int, b: int) -> tuple:
    if b == 0:
        return (1, 0)
    x, y = bezouts_identity_solution(b, a % b)
    return (y, x - (a // b) * y)
