def angle_difference(angle1: float, angle2: float) -> float:
    diff = abs(angle1 - angle2) % 360
    return min(diff, 360 - diff)
