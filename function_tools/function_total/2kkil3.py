def vector_projection(v: tuple, a: tuple) -> tuple:
    av_product = sum(x * y for x, y in zip(v, a))
    aa_product = sum(x * x for x in a)
    scalar = av_product / aa_product
    return tuple(scalar * x for x in a)
