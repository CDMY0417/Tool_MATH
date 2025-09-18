def z_range_for_integer_lattice_points(lower_bound: float, upper_bound: float):
    z_min = int(lower_bound) + (1 if lower_bound % 1 != 0 else 0)
    z_max = int(upper_bound)
    return range(z_min, z_max + 1)
