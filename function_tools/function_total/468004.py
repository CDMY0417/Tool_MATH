def midpoint_coordinates(x_coords: list[float]) -> list[float]:
    return [(x_coords[i] + x_coords[(i + 1) % len(x_coords)]) / 2 for i in range(len(x_coords))]
