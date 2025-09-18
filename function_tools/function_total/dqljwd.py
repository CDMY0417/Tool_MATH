def power_of_fraction(numerator: int, denominator: int, exponent: int) -> str:
    num_power = numerator ** exponent
    denom_power = denominator ** exponent
    return f'{num_power}/{denom_power}'
