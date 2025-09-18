def isosceles_triangle_count(triangles: list[list[float]]) -> int:
    count = 0
    for triangle in triangles:
        if len(set(triangle)) == 2:  # Two sides must be equal
            count += 1
    return count
