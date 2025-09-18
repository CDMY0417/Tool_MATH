def perpendicular_slope(slope: float) -> float:
    if slope == 0:
        return float('inf')
    elif slope == float('inf'):
        return 0
    return -1 / slope
