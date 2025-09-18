def smaller_clock_angle(angle1: float, angle2: float) -> float:
    difference = abs(angle1 - angle2)
    return min(difference, 360 - difference)
