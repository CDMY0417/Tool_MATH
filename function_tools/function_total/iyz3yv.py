import math

def coordinates_of_point_on_unit_circle(angle_degrees: float) -> tuple:
    radians = math.radians(angle_degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
