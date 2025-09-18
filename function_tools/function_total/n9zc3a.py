def area_of_full_circles(semicircles: int, radius: int) -> float:
    full_circles = semicircles / 2
    total_area = full_circles * (radius ** 2) * 3.141592653589793
    return total_area
