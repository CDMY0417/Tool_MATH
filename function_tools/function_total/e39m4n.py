def evaluate_power(base: int, exponent: int) -> int:
    if base < 0:
        if exponent % 2 == 0:
            return (-base) ** exponent
        else:
            return -((-base) ** exponent)
    else:
        return base ** exponent
