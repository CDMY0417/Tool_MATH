def slope_of_line(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    if x2 == x1:
        return float('inf') # vertical line
    return (y2 - y1) / (x2 - x1)
