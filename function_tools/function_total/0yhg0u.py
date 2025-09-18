def total_area_of_shapes(areas: list[float], counts: list[int]) -> float:
    return sum([area * count for area, count in zip(areas, counts)])
