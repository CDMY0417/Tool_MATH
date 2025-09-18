def cartesian_coordinates_on_sphere(latitude: float, longitude: float, radius: float):
    from math import radians, sin, cos
    lat_rad = radians(latitude)
    lon_rad = radians(longitude)
    x = radius * sin(lat_rad) * cos(lon_rad)
    y = radius * sin(lat_rad) * sin(lon_rad)
    z = radius * cos(lat_rad)
    return (x, y, z)
