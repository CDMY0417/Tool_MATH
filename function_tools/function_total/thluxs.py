def sphere_volume_to_radius(volume: float) -> float:
    r_cubed = (3 * volume) / (4 * 3.141592653589793)
    return r_cubed ** (1/3)
