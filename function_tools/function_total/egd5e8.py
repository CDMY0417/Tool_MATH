from math import pi

def spheres_volume(number_of_spheres: int, fraction: float, radius: int) -> float:
    sphere_volume = (4/3) * pi * (radius ** 3)
    return number_of_spheres * fraction * sphere_volume
