def distance_from_point(px: int, py: int, cx: int, cy: int, r_squared: int):
    return ((px - cx) ** 2 + (py - cy) ** 2 + r_squared) ** 0.5
