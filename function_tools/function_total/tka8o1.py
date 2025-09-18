def vector_projection(v: tuple, w: tuple) -> tuple:
    dot_product_vw = sum(vi * wi for vi, wi in zip(v, w))
    dot_product_ww = sum(wi * wi for wi in w)
    projection_factor = dot_product_vw / dot_product_ww
    return tuple(projection_factor * wi for wi in w)
