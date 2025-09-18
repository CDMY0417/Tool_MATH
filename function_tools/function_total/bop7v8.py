def vector_triple_product(u: tuple, v: tuple, w: tuple):
    u_dot_w = sum(u_i * w_i for u_i, w_i in zip(u, w))
    u_dot_v = sum(u_i * v_i for u_i, v_i in zip(u, v))
    result = tuple(u_dot_w * v_i - u_dot_v * w_i for v_i, w_i in zip(v, w))
    return result
