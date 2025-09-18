def normalize_angle(angle: int) -> int:
    normalized_angle = angle % 180
    if normalized_angle > 90:
        normalized_angle -= 180
    return normalized_angle
