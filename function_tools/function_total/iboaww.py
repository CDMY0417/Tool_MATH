def check_isosceles_by_angles(angles: list[float]) -> bool:
    return len(set(angles)) == 2  # Two angles must be equal
