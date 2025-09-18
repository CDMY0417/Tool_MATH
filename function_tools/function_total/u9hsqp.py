def find_linear_remainder(p: int, q: int, f_p: int, f_q: int):
    a = (f_q - f_p) // (q - p)
    b = f_p - a * p
    return a, b
