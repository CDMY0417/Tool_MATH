def dot_product(a: tuple, b: tuple) -> float:
    return sum(a[i] * b[i] for i in range(len(a)))
