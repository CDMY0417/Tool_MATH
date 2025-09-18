def expand_quadratic(a: int, b: int, c: int, d: int):
    ac = a * c
    bd = b * d
    ad_bc = a * d + b * c
    return ac, ad_bc, bd
