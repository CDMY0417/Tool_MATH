def are_lines_parallel(direction_vector1: tuple[float, float, float], direction_vector2: tuple[float, float, float]) -> bool:
    return (direction_vector1[0] / direction_vector2[0] == direction_vector1[1] / direction_vector2[1] == direction_vector1[2] / direction_vector2[2])
