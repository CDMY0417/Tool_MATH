def sector_area(radius: float, angle_degrees: float) -> float:
    angle_radians = (angle_degrees / 360) * 2 * 3.14159
    return 0.5 * radius**2 * angle_radians
