def ellipse_major_minor_axes_from_area(area: float, minor_axis_length: float):
    import math
    major_axis_length = area / (math.pi * minor_axis_length)
    return major_axis_length
