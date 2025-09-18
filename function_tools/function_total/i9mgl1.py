def area_of_triangle_using_coordinates(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
