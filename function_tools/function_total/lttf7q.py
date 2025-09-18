def convert_units(amount: float, conversion_factors: list[float]):
    result = amount
    for factor in conversion_factors:
        result *= factor
    return result
