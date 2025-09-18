def vector_triple_product(p: tuple, q: tuple, r: tuple):
    return tuple((p[i] * sum(q[j] * r[j] for j in range(len(r))) - r[i] * sum(p[j] * q[j] for j in range(len(q)))) for i in range(len(p)))
