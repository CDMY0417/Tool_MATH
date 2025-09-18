def cancel_common_factor(numerator: int, denominator: int, factor: int) -> tuple:
    return (numerator // factor, denominator // factor) if factor != 0 else (numerator, denominator)
