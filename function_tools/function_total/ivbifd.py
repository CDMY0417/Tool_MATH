def convert_units(quantity: float, conversion_factors: list[float]) -> float:
    result = quantity
    for factor in conversion_factors:
        result *= factor
    return result
