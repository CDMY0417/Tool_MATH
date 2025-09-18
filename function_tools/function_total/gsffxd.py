def are_vectors_proportional(u: tuple[float, float, float], v: tuple[float, float, float]) -> bool:
    if u == (0, 0, 0) or v == (0, 0, 0):
        return False
    factor = None
    for u_comp, v_comp in zip(u, v):
        if v_comp != 0:
            if factor is None:
                factor = u_comp / v_comp
            elif factor != u_comp / v_comp:
                return False
    return factor is not None
