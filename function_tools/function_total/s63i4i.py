def parameterize_line(start: tuple[float, float], end: tuple[float, float], t: float):
    return (start[0] + t * (end[0] - start[0]), start[1] + t * (end[1] - start[1]))
