def calculate_cylinder_volume(height: float, circumference: float) -> float:
    radius = circumference / (2 * 3.141592653589793)
    volume = 3.141592653589793 * radius ** 2 * height
    return volume
