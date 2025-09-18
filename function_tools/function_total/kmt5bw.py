def distance_between_ellipse_foci(major_axis_length: float, minor_axis_length: float) -> float:
    c = ((major_axis_length / 2)**2 - (minor_axis_length / 2)**2)**0.5
    return 2 * c
