def cosine_from_tangent_half_angle(tan_half_angle: float) -> float:
    return (1 - tan_half_angle ** 2) / (1 + tan_half_angle ** 2)
