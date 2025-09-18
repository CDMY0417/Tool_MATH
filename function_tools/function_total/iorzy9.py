def isosceles_triangle_altitude(base: float, equal_side: float) -> float:
    half_base = base / 2
    return (equal_side**2 - half_base**2)**0.5
