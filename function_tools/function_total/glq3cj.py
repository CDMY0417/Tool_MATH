def calculate_sector_angle(radius: float, height: float, circumference: float) -> float:
    import math
    sweep_radius = math.sqrt(radius**2 + height**2)
    angle = circumference / sweep_radius
    return angle
