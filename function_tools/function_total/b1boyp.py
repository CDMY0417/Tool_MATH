def find_equivalent_angle(angle: int, lower_bound: int, upper_bound: int):
    normalized_angle = angle % 360
    if lower_bound <= normalized_angle <= upper_bound:
        return normalized_angle
    return None
