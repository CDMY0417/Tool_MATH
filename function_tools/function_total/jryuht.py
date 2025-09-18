def parameterize_line(base: tuple, direction: tuple, t: float) -> tuple:
    x = base[0] + direction[0] * t
    y = base[1] + direction[1] * t
    return (x, y)
