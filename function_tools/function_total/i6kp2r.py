def scale_vector_to_coordinate(v: tuple, coordinate: int, value: int):
    scale = value / v[coordinate]
    return tuple(x * scale for x in v)
