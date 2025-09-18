def normalize_angle(angle: float, period: float) -> float:
    return angle - (int(angle / period) * period)
