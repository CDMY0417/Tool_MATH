def scalar_multiply_vector(k: float, v: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(k * vi for vi in v)
