def dot_product(u: tuple, v: tuple) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))
