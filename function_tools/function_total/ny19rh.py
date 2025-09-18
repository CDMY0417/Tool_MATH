def coordinates_on_unit_circle(angle: float):
    import math
    radians = math.radians(angle)
    x = math.cos(radians)
    y = math.sin(radians)
    return (x, y)
