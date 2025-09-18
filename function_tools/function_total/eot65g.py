def rectangular_to_spherical_phi(rho: float, z: float) -> float:
    from math import acos
    return acos(z / rho)
