def foci_of_ellipse(semi_major_axis: float, semi_minor_axis: float) -> tuple:
    c = (semi_major_axis**2 - semi_minor_axis**2)**0.5
    return (c, 0), (-c, 0)
