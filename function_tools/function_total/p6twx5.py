def vector_triple_product(a: tuple, b: tuple, c: tuple):
    dot_a_c = sum(ac * cc for ac, cc in zip(a, c))
    dot_a_b = sum(ab * bb for ab, bb in zip(a, b))
    b_component = tuple(bb * dot_a_c for bb in b)
    c_component = tuple(cc * dot_a_b for cc in c)
    return tuple(bc - cc for bc, cc in zip(b_component, c_component))
