def ellipse_axes_lengths(a_squared: float, b_squared: float):
    semimajor = max(a_squared, b_squared) ** 0.5
    semiminor = min(a_squared, b_squared) ** 0.5
    return semimajor, semiminor
