def is_scalar_multiple(a: tuple, b: tuple) -> bool:
    if a[0] * b[1] == a[1] * b[0]:
        return (a[0] != 0 or a[1] != 0) and (b[0] != 0 or b[1] != 0)
    return False
