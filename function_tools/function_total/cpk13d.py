def cube_root(number: float):
    return number ** (1/3) if number >= 0 else -(-number) ** (1/3)
