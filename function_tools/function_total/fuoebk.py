def apply_radical_conjugate_to_product(p1: int, q1: int, p2: int, q2: int, r: int):
    return p1*p2 + p1*q2*(r**0.5) + q1*p2*(r**0.5) + q1*q2*r
