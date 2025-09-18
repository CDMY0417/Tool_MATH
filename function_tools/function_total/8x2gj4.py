def am_gm_inequality(x1: float, x2: float, x3: float, x4: float) -> bool:
    return (x1 + x2 + x3 + x4) / 4 >= (x1 * x2 * x3 * x4)**(1/4)
